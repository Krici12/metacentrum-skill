#!/usr/bin/env python3
"""Extract the main article content of a docs.e-infra.cz family page into Markdown.

The docs sites (docs.metacentrum.cz, docs.cerit.io, docs.du.cesnet.cz,
docs.account.e-infra.cz) are Next.js SSR apps. The <main> article is rendered
markdown, so we walk the DOM of the article container and emit Markdown that
faithfully mirrors the source (headings, paragraphs, code, lists, tables, links).

Uses only the Python standard library (html.parser).

Usage:
    python3 extract.py <input.html> [output.md]
"""
import html
import re
import sys
from html.parser import HTMLParser


# ---- block-level tags where we break lines ----
BLOCK = {
    "p", "div", "section", "li", "ul", "ol", "h1", "h2", "h3", "h4", "h5",
    "pre", "code", "blockquote", "table", "tr", "td", "th", "hr", "br",
    "details", "summary", "figure", "figcaption", "article", "aside",
}
# tags we fully skip (navigation, scripts, icons, images)
SKIP = {"script", "style", "nav", "svg", "path", "head", "meta", "link",
        "button", "header", "footer", "select", "option", "template", "noscript"}


class ArticleExtractor(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.out = []
        self.skip_depth = 0
        self.pre_depth = 0
        self.code_depth = 0
        self.a_href = None
        self.a_buf = []
        self.in_article = False
        self.article_sel_depth = 0
        self.pending_nl = False  # a newline is queued (block break)
        self.table_open = False
        self.last_was_blank = False

    # ---------- helpers ----------
    def push(self, s):
        self.out.append(s)

    def newline(self):
        if self.out and not self.last_was_blank:
            self.pending_nl = True

    def emit_pending_newline(self):
        if self.pending_nl and self.out and not self.pending_nl:
            return
        if self.pending_nl:
            # collapse to a single newline
            if self.out and self.out[-1] != "\n":
                self.out.append("\n")
            self.pending_nl = False

    # ---------- parser callbacks ----------
    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        cls = a.get("class", "")

        # article container heuristic: any <main> or an element with article/prose class
        if tag == "main":
            self.in_article = True
            self.article_sel_depth = 0
        if not self.in_article and ("article" in cls or "prose" in cls or "nd-content" in cls):
            self.in_article = True
            self.article_sel_depth = 0
        if self.in_article:
            self.article_sel_depth += 1

        if tag in SKIP:
            if self.in_article:
                self.skip_depth += 1
            return

        if tag == "pre":
            self.pre_depth += 1
            self.emit_pending_newline()
            self.push("\n```\n")
            return
        if tag == "code" and self.pre_depth == 0:
            # inline code unless inside pre
            if self.in_article:
                self.push("`")
            self.code_depth += 1
            return

        if tag.startswith("h") and tag in {"h1","h2","h3","h4","h5","h6"}:
            self.emit_pending_newline()
            self.push("\n" + "#" * int(tag[1]) + " ")
            return
        if tag == "p":
            self.emit_pending_newline()
            self.push("\n")
            return
        if tag == "li":
            self.emit_pending_newline()
            self.push("\n- ")
            return
        if tag == "br":
            self.push("\n")
            return
        if tag == "hr":
            self.emit_pending_newline()
            self.push("\n---\n")
            return
        if tag == "blockquote":
            self.emit_pending_newline()
            self.push("\n> ")
            return
        if tag == "strong" or tag == "b":
            self.push("**")
            return
        if tag == "em" or tag == "i":
            self.push("*")
            return
        if tag == "a":
            href = a.get("href")
            if href:
                self.a_href = href
                self.a_buf = []
            return
        if tag == "table":
            self.emit_pending_newline()
            self.push("\n")
            self.table_open = True
            return
        if tag == "tr":
            self.push("| ")
            return
        if tag in ("td", "th"):
            if self.a_href is None:  # simple cell
                pass
            return
        if tag == "details":
            self.emit_pending_newline()
            self.push("\n<details>\n")
            return
        if tag == "summary":
            self.push("<summary>")
            return
        if tag == "ul":
            self.emit_pending_newline()
            return
        if tag == "ol":
            self.emit_pending_newline()
            return

    def handle_endtag(self, tag):
        if tag in SKIP:
            if self.skip_depth > 0:
                self.skip_depth -= 1
            return

        if tag == "pre":
            self.pre_depth -= 1
            self.push("\n```\n")
            return
        if tag == "code" and self.pre_depth == 0:
            if self.code_depth > 0:
                self.code_depth -= 1
                if self.in_article:
                    self.push("`")
            return

        if tag == "a" and self.a_href is not None:
            text = "".join(self.a_buf).strip()
            if text:
                self.push(f"[{text}]({self.a_href})")
            self.a_href = None
            self.a_buf = []
            return
        if tag in ("strong", "b"):
            self.push("**")
            return
        if tag in ("em", "i"):
            self.push("*")
            return
        if tag == "p":
            self.emit_pending_newline()
            self.push("\n\n")
            self.last_was_blank = True
            return
        if tag == "li":
            self.emit_pending_newline()
            return
        if tag in ("h1","h2","h3","h4","h5","h6","blockquote"):
            self.emit_pending_newline()
            self.push("\n")
            return
        if tag == "td" or tag == "th":
            self.push(" |")
            return
        if tag == "tr":
            self.push("\n")
            return
        # block-level end -> newline
        if tag in BLOCK:
            self.emit_pending_newline()
            self.push("\n")
            return

    def handle_startendtag(self, tag, attrs):
        if tag == "br":
            self.push("\n")
        elif tag == "hr":
            self.emit_pending_newline()
            self.push("\n---\n")
        elif tag == "img":
            a = dict(attrs)
            alt = a.get("alt", "")
            src = a.get("src", "")
            # skip branding/logos from the page header; keep real article images
            if "/img/" in src or "/logo" in src:
                return
            if alt or src:
                self.push(f"![{alt}]({src})")

    def handle_data(self, data):
        if self.skip_depth:
            return
        if not self.in_article:
            return
        if self.pre_depth:
            # keep code verbatim
            self.push(data)
            return
        if self.a_href is not None:
            self.a_buf.append(data)
            return
        text = html.unescape(data)
        # collapse runs of whitespace to single spaces for normal text
        text = re.sub(r"[ \t]+", " ", text)
        self.push(text)


def main():
    inp, outp = sys.argv[1], sys.argv[2] if len(sys.argv) > 2 else None
    html_src = open(inp, encoding="utf-8", errors="replace").read()

    # Trim to the article region if a <main> exists to reduce noise
    p = ArticleExtractor()
    p.feed(html_src)
    raw = "".join(p.out)

    # Post-process: collapse 3+ newlines to 2, strip leading/trailing space per line
    raw = re.sub(r"\n{3,}", "\n\n", raw)
    raw = re.sub(r" *\n", "\n", raw)
    raw = raw.strip() + "\n"

    if outp:
        with open(outp, "w", encoding="utf-8") as f:
            f.write(raw)
        print(f"wrote {len(raw)} bytes -> {outp}")
    else:
        sys.stdout.write(raw)


if __name__ == "__main__":
    main()
