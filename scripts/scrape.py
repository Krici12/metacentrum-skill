#!/usr/bin/env python3
"""Fetch the e-INFRA CZ documentation pages and store them in raw/ mirroring
the site's URL structure.

The docs are spread across several e-INFRA CZ domains:
    docs.metacentrum.cz   - MetaCentrum grid (PBS/qsub, modules, GPU, Jupyter, OnDemand)
    docs.cerit.io         - CERIT-SC Kubernetes / Rancher / JupyterHub / workflows
    docs.du.cesnet.cz     - data storage services (S3 object storage, RBD)
    docs.account.e-infra.cz - e-INFRA CZ account management / auth

Each URL is mapped to raw/<section>/<path>.md where <path> mirrors the part of
the URL after the docs root, so the tree stays diffable and re-scrapable.

Usage:
    python3 scripts/scrape.py            # scrape everything (respects raw/ already-fetched)
    python3 scripts/scrape.py --fresh    # re-fetch even if file exists
"""
import argparse
import os
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RAW = os.path.join(ROOT, "raw")

# "topic" -> list of (url, local_path)
SITES = {
    # domain prefix dictionary: full url -> local path
}

# Explicit mapping.  src: absolute URL, dst: local path under raw/
# The local tree mirrors the site structure (section == top-level category).
MAP = [
    # ---------------- MetaCentrum grid: PBS / jobs / queues / walltime ----------------
    ("https://docs.metacentrum.cz/en/docs/computing/run-basic-job", "metacentrum/computing/run-basic-job.md"),
    ("https://docs.metacentrum.cz/en/docs/computing/resources/pbs-commands", "metacentrum/computing/resources/pbs-commands.md"),
    ("https://docs.metacentrum.cz/en/docs/computing/resources/queues", "metacentrum/computing/resources/queues.md"),
    ("https://docs.metacentrum.cz/en/docs/computing/resources/resources", "metacentrum/computing/resources/resources.md"),
    ("https://docs.metacentrum.cz/en/docs/computing/resources/qsub-compiler", "metacentrum/computing/resources/qsub-compiler.md"),
    ("https://docs.metacentrum.cz/en/docs/computing/resources/fairshare", "metacentrum/computing/resources/fairshare.md"),
    ("https://docs.metacentrum.cz/en/docs/computing/jobs/email-notif", "metacentrum/computing/jobs/email-notif.md"),
    ("https://docs.metacentrum.cz/en/docs/computing/jobs/extend-walltime", "metacentrum/computing/jobs/extend-walltime.md"),
    ("https://docs.metacentrum.cz/en/docs/computing/jobs/finished-jobs", "metacentrum/computing/jobs/finished-jobs.md"),
    ("https://docs.metacentrum.cz/en/docs/computing/jobs/job-arrays", "metacentrum/computing/jobs/job-arrays.md"),
    ("https://docs.metacentrum.cz/en/docs/computing/jobs/job-tracking", "metacentrum/computing/jobs/job-tracking.md"),
    ("https://docs.metacentrum.cz/en/docs/computing/jobs/modify-job-attributes", "metacentrum/computing/jobs/modify-job-attributes.md"),
    ("https://docs.metacentrum.cz/en/docs/computing/jobs/trap-command", "metacentrum/computing/jobs/trap-command.md"),
    ("https://docs.metacentrum.cz/en/docs/computing/advanced", "metacentrum/computing/advanced.md"),
    ("https://docs.metacentrum.cz/en/docs/computing/parallel-comput", "metacentrum/computing/parallel-comput.md"),
    ("https://docs.metacentrum.cz/en/docs/computing/infrastructure/frontends", "metacentrum/computing/infrastructure/frontends.md"),
    ("https://docs.metacentrum.cz/en/docs/computing/infrastructure/frontend-storage", "metacentrum/computing/infrastructure/frontend-storage.md"),
    ("https://docs.metacentrum.cz/en/docs/computing/infrastructure/storages", "metacentrum/computing/infrastructure/storages.md"),
    ("https://docs.metacentrum.cz/en/docs/computing/infrastructure/mount-storages", "metacentrum/computing/infrastructure/mount-storages.md"),
    ("https://docs.metacentrum.cz/en/docs/computing/infrastructure/scratch-storages", "metacentrum/computing/infrastructure/scratch-storages.md"),
    ("https://docs.metacentrum.cz/en/docs/computing/infrastructure/specific-nodes", "metacentrum/computing/infrastructure/specific-nodes.md"),
    ("https://docs.metacentrum.cz/en/docs/computing/my-metacentrum", "metacentrum/computing/my-metacentrum.md"),

    # ---------------- MetaCentrum: GPU nodes ----------------
    ("https://docs.metacentrum.cz/en/docs/computing/gpu-comput/gpu-job", "metacentrum/computing/gpu-comput/gpu-job.md"),
    ("https://docs.metacentrum.cz/en/docs/computing/gpu-comput/dgx", "metacentrum/computing/gpu-comput/dgx.md"),
    ("https://docs.metacentrum.cz/en/docs/computing/gpu-comput/clusters", "metacentrum/computing/gpu-comput/clusters.md"),
    ("https://docs.metacentrum.cz/en/docs/computing/gpu-comput/nvidia", "metacentrum/computing/gpu-comput/nvidia.md"),

    # ---------------- MetaCentrum: software modules ----------------
    ("https://docs.metacentrum.cz/en/docs/software/modules", "metacentrum/software/modules.md"),
    ("https://docs.metacentrum.cz/en/docs/software/install-software", "metacentrum/software/install-software.md"),
    ("https://docs.metacentrum.cz/en/docs/software/containers", "metacentrum/software/containers.md"),
    ("https://docs.metacentrum.cz/en/docs/software/search-soft", "metacentrum/software/search-soft.md"),
    ("https://docs.metacentrum.cz/en/docs/software/graphical-access", "metacentrum/software/graphical-access.md"),
    ("https://docs.metacentrum.cz/en/docs/software/sw-list/jupyter", "metacentrum/software/sw-list/jupyter.md"),

    # ---------------- MetaCentrum: data / storage ----------------
    ("https://docs.metacentrum.cz/en/docs/data/types-of-storage", "metacentrum/data/types-of-storage.md"),
    ("https://docs.metacentrum.cz/en/docs/data/direct-access-storages", "metacentrum/data/direct-access-storages.md"),
    ("https://docs.metacentrum.cz/en/docs/data/quotas", "metacentrum/data/quotas.md"),
    ("https://docs.metacentrum.cz/en/docs/data/large-data", "metacentrum/data/large-data.md"),
    ("https://docs.metacentrum.cz/en/docs/data/data-sharing", "metacentrum/data/data-sharing.md"),
    ("https://docs.metacentrum.cz/en/docs/data/metacentrum-backup", "metacentrum/data/metacentrum-backup.md"),

    # ---------------- MetaCentrum: authentication (kerberos / ssh) ----------------
    ("https://docs.metacentrum.cz/en/docs/access/security/kerberos", "metacentrum/access/security/kerberos.md"),
    ("https://docs.metacentrum.cz/en/docs/access/security/connect-auth", "metacentrum/access/security/connect-auth.md"),
    ("https://docs.metacentrum.cz/en/docs/access/log-in", "metacentrum/access/log-in.md"),
    ("https://docs.metacentrum.cz/en/docs/access/account", "metacentrum/access/account.md"),

    # ---------------- MetaCentrum: OnDemand + web apps ----------------
    ("https://docs.metacentrum.cz/en/docs/graphical/ondemand", "metacentrum/graphical/ondemand.md"),
    ("https://docs.metacentrum.cz/en/docs/graphical/usegalaxy", "metacentrum/graphical/usegalaxy.md"),

    # ---------------- CERIT-SC: Kubernetes ----------------
    ("https://docs.cerit.io/en/docs/platform/overview", "cerit/platform/overview.md"),
    ("https://docs.cerit.io/en/docs/platform/access", "cerit/platform/access.md"),
    ("https://docs.cerit.io/en/docs/platform/hw", "cerit/platform/hw.md"),
    ("https://docs.cerit.io/en/docs/platform/technologies", "cerit/platform/technologies.md"),
    ("https://docs.cerit.io/en/docs/rancher/rancher", "cerit/rancher/rancher.md"),
    ("https://docs.cerit.io/en/docs/rancher/quotas", "cerit/rancher/quotas.md"),
    ("https://docs.cerit.io/en/docs/rancher/reqproj", "cerit/rancher/reqproj.md"),
    ("https://docs.cerit.io/en/docs/kubernetes/kubectl", "cerit/kubernetes/kubectl.md"),
    ("https://docs.cerit.io/en/docs/kubernetes/ns", "cerit/kubernetes/ns.md"),
    ("https://docs.cerit.io/en/docs/kubernetes/job", "cerit/kubernetes/job.md"),
    ("https://docs.cerit.io/en/docs/kubernetes/pvc", "cerit/kubernetes/pvc.md"),
    ("https://docs.cerit.io/en/docs/kubernetes/resources", "cerit/kubernetes/resources.md"),
    ("https://docs.cerit.io/en/docs/kubernetes/expose", "cerit/kubernetes/expose.md"),
    ("https://docs.cerit.io/en/docs/kubernetes/security", "cerit/kubernetes/security.md"),
    ("https://docs.cerit.io/en/docs/docker/limitations", "cerit/docker/limitations.md"),
    ("https://docs.cerit.io/en/docs/docker/dockerfile", "cerit/docker/dockerfile.md"),

    # ---------------- CERIT-SC: JupyterHub / web apps ----------------
    ("https://docs.cerit.io/en/docs/web-apps/jupyterhub", "cerit/web-apps/jupyterhub.md"),
    ("https://docs.cerit.io/en/docs/web-apps/binderhub", "cerit/web-apps/binderhub.md"),

    # ---------------- CERIT-SC: AI as a Service (AIaaS) ----------------
    ("https://docs.cerit.io/en/docs/ai-as-a-service/introduction", "cerit/ai-as-a-service/introduction.md"),
    ("https://docs.cerit.io/en/docs/ai-as-a-service/ai-api", "cerit/ai-as-a-service/ai-api.md"),
    ("https://docs.cerit.io/en/docs/ai-as-a-service/chat-ai", "cerit/ai-as-a-service/chat-ai.md"),
    ("https://docs.cerit.io/en/docs/ai-as-a-service/mcp", "cerit/ai-as-a-service/mcp.md"),
    ("https://docs.cerit.io/en/docs/ai-as-a-service/llm-integration", "cerit/ai-as-a-service/llm-integration.md"),
    ("https://docs.cerit.io/en/docs/ai-as-a-service/deepsite", "cerit/ai-as-a-service/deepsite.md"),
    ("https://docs.cerit.io/en/docs/ai-as-a-service/deepsec", "cerit/ai-as-a-service/deepsec.md"),
    ("https://docs.cerit.io/en/docs/ai-as-a-service/ai-data-privacy", "cerit/ai-as-a-service/ai-data-privacy.md"),
    ("https://docs.cerit.io/en/docs/ai-as-a-service/n8n-agents", "cerit/ai-as-a-service/n8n-agents.md"),

    # ---------------- CESNET DU: object storage / S3 ----------------
    ("https://docs.du.cesnet.cz/en/docs/object-storage-s3/s3-service", "cesnet/object-storage-s3/s3-service.md"),
    ("https://docs.du.cesnet.cz/en/docs/object-storage-s3/s3-getting-access", "cesnet/object-storage-s3/s3-getting-access.md"),
    ("https://docs.du.cesnet.cz/en/docs/object-storage-s3/aws-cli", "cesnet/object-storage-s3/aws-cli.md"),
    ("https://docs.du.cesnet.cz/en/docs/object-storage-s3/s3cmd", "cesnet/object-storage-s3/s3cmd.md"),
    ("https://docs.du.cesnet.cz/en/docs/object-storage-s3/s3-features", "cesnet/object-storage-s3/s3-features.md"),
    ("https://docs.du.cesnet.cz/en/docs/object-storage-s3/s3-use-cases", "cesnet/object-storage-s3/s3-use-cases.md"),
    ("https://docs.du.cesnet.cz/en/docs/object-storage-s3/rclone", "cesnet/object-storage-s3/rclone.md"),
    ("https://docs.du.cesnet.cz/en/docs/object-storage-s3/boto3", "cesnet/object-storage-s3/boto3.md"),

    # ---------------- e-INFRA CZ account / auth ----------------
    ("https://docs.account.e-infra.cz/en/docs/access/account", "einfra-account/access/account.md"),
    ("https://docs.account.e-infra.cz/en/docs/access/perun", "einfra-account/access/perun.md"),
    ("https://docs.account.e-infra.cz/en/docs/access/mfa", "einfra-account/access/mfa.md"),
    ("https://docs.account.e-infra.cz/en/docs/access/orcid", "einfra-account/access/orcid.md"),
]


def fetch(src):
    """curl the page; returns (html, ok)."""
    r = subprocess.run(
        ["curl", "-sL", "-A", "Mozilla/5.0 (scrape; e-INFRA docs mirror)", src],
        capture_output=True, text=True)
    return r.stdout, r.returncode == 0


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--fresh", action="store_true",
                    help="re-fetch even when the file already exists")
    args = ap.parse_args()

    ok, failed, skipped = [], [], 0
    for src, dst in MAP:
        path = os.path.join(RAW, dst)
        if not args.fresh and os.path.exists(path) and os.path.getsize(path) > 0:
            skipped += 1
            continue
        html, fetched = fetch(src)
        if not fetched or "<title>404" in html or len(html) < 5000:
            failed.append((src, "fetch-failed-or-404" if fetched else "network"))
            continue
        os.makedirs(os.path.dirname(path), exist_ok=True)
        tmp = path + ".tmp.html"
        with open(tmp, "w", encoding="utf-8") as f:
            f.write(html)
        # extract via the sibling extractor
        r = subprocess.run(
            ["python3", os.path.join(ROOT, "scripts", "extract.py"), tmp, path],
            capture_output=True, text=True)
        if os.path.exists(tmp):
            os.remove(tmp)
        if not fetched or (r.returncode != 0) or not os.path.exists(path):
            failed.append((src, r.stderr.strip()))
            continue
        ok.append(dst)

    print(f"written: {len(ok)}  skipped(existing): {skipped}  failed: {len(failed)}")
    for src, why in failed:
        print(f"  FAIL {why}  {src}")
    if ok:
        print("updated:")
        for d in ok:
            print(f"  {d}")


if __name__ == "__main__":
    main()
