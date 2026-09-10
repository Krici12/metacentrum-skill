# AI as a Service (AIaaS) — CERIT-SC / e-INFRA CZ

> Praktická příručka. Zdroj: `raw/cerit/ai-as-a-service/` (introduction, ai-api,
> chat-ai, mcp, llm-integration, deepsite, deepsec, ai-data-privacy, n8n-agents)
> a `raw/cerit/web-apps/jupyterhub.md` (AI obrazy / Claude Code v Jupyteru).

## Co to je

CERIT-SC provozuje **on-premise AI platformu** v rámci e-INFRA CZ (NVIDIA
DGX-H100/B200/B300). Běží na ní **otevřené LLM a generativní modely**
(Kimi, GLM, DeepSeek, Qwen, gpt-oss…). Vše běží lokálně v infrastruktuře —
**žádné dotazy neodchází k externím providerům** (s výjimkou vyhledávání na
internetu). Platforma je vhodná i pro citlivější/privátní výzkum (viz
`ai-data-privacy.md`).

Přístup: studenti/zaměstnanci MUNI a uživatelé MetaCentra.

## Hlavní služby (inference)

| Služba | URL / endpoint | Použití |
|--------|----------------|---------|
| **Chat UI (Open WebUI)** | https://chat.ai.e-infra.cz | konverzační rozhraní, výběr modelu, image gen, RAG na dokument, nástroje (web/GitHub/arXiv, Python sandbox) |
| **OpenAI-kompatibilní API** | `https://llm.ai.e-infra.cz/v1/` | skripty, pipeline, frameworky |
| **MCP servery** | `https://llm.ai.e-infra.cz/<name>/mcp` | MCP integrace pro agenty |
| **AI coding assistants** | viz `llm-integration.md` | Claude Code, Codex, OpenCode, VS Code, JetBrains |
| **DeepSite** | DeepSite | generování web stránek/aplikací z textu (vibe coding) |
| **n8n** | n8n Agents | low-code workflow + AI agenti |
| **DeepSec** | DeepSec | AI skener zranitelností kódu |
| **Jupyter AI** | hub.cloud.e-infra.cz | AI asistent přímo v notebooku (viz `jupyterhub.md`) |

Stav modelů: https://llm.ai.e-infra.cz/status/ · vlastní spotřeba tokenů (API):
https://llm.ai.e-infra.cz/usage

## OpenAI-kompatibilní API — rychlý start

Předpoklad: MetaCentrum (nebo MUNI) účet. **API key vygeneruješ v Open WebUI**:
`Settings → Account → API keys` (ne JWT; vygeneruj/nech zobrazit), a **nikdy ho
nesdílej** (porušení podmínek → okamžité zablokování).

### Výpis modelů a chat completions

```bash
export E_INFRA_API_TOKEN=sk-...

# seznam dostupných modelů
curl -H "Authorization: Bearer ${E_INFRA_API_TOKEN}" \
     https://llm.ai.e-infra.cz/v1/models | jq .data[].id

# chat (OpenAI formát)
curl https://llm.ai.e-infra.cz/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer ${E_INFRA_API_TOKEN}" \
  -d '{"model":"mini","messages":[{"role":"user","content":"..."}]}'
```

- Aktuální modely (výběr): `gpt-oss-120b`, `deepseek-v4-flash`/`-pro`,
  `glm-5.3`, `kimi-k3`, `qwen3.5-int4`, `qwen3.8-flash-next`, `qwen3.8-27b`,
  `mistral-medium-3.5`, `gemma4`. Jména jsou case-sensitive, mohou mít
  quantizační sufix (např. `qwen3.5-int4`). Živý seznam:
  https://llm.ai.e-infra.cz/status/
- **Praktické aliasy** (verzově nezávislé, vždy míří na aktuální doporučený
  model): `agentic`/`coder` → `qwen3.8-flash-next`, `mini` → `gpt-oss-120b`,
  `thinker`/`deepseek-thinking` → `deepseek-v4-flash-thinking`,
  `deepseek` → `deepseek-v4-flash` (reasoning defaultně vypnutý),
  `glm`/`glm-5` → `glm-5.3`, `kimi` → `kimi-k3`, `qwen3.5` → `qwen3.5-int4`.
  Pro dlouhodobě stabilní kód preferuj aliasy.
- Metadata modelů (capabilities, context_size, quantization):
  `curl ... https://llm.ai.e-infra.cz/v1/model/info | jq '[.data[] | {model_name, capabilities: .model_info.capabilities, context_size: .model_info.context_size}]'`

### Konfigurace frameworků

OpenAI-kompatibilní → funguje s LangChain, LlamaIndex, PydanticAI, FastAPI atd.
Příklad PydanticAI:
```python
from pydantic_ai_provider import OpenAIModel, OpenAIProvider
import os
model = OpenAIModel('deepseek', provider=OpenAIProvider(
    base_url="https://llm.ai.e-infra.cz/v1",
    api_key=os.getenv("E_INFRA_API_TOKEN"),
))
```

### Reasoningové modely

- **DeepSeek** běží defaultně **bez** reasoning → zapneš přes
  `"chat_template_kwargs": {"thinking": true}`, nebo použij variantu
  **`deepseek-thinking`** (vždy v thinking módu) pro prostředí bez `chat_template_kwargs`.
- V chat UI jsou hybridní modely většinou přednastavené na reasoning.

## MCP servery

- Jsou dostupné přes `https://llm.ai.e-infra.cz/<servername>/mcp`.
- **Doporučeno: `"stream": true`** pro MCP requesty — jinak hrozí HTTP 408
  (infrastrukturní timeout pro non-streaming je 30 min a nejde přepsat).

## AI coding asistenti (Claude Code / Codex / OpenCode / IDE)

> Následující nastavení směruje vaše lokální nástroje na **CERIT-SC / e-INFRA
> CZ backend** (`llm.ai.e-infra.cz`), ne na komerční API. Je to návod z oficiální
> dokumentace e-INFRA CZ.

### Claude Code (CLI)

```bash
export ANTHROPIC_BASE_URL="https://llm.ai.e-infra.cz/"
export ANTHROPIC_AUTH_TOKEN="sk-..."                 # API key z chat.ai.e-infra.cz
export ANTHROPIC_MODEL="agentic"
export ANTHROPIC_DEFAULT_OPUS_MODEL="thinker"
export ANTHROPIC_DEFAULT_SONNET_MODEL="agentic"
export ANTHROPIC_DEFAULT_HAIKU_MODEL="mini"
export CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC=1
claude [project-dir]
```

- První spuštění: projdi výběr schématu syntaxe, u „Select login method" ukonči
  (Ctrl+C ×3) a v `~/.claude.json` přidej `"hasCompletedOnboarding": true`
  (ověř validní JSON). Nebo nastav proměnné v `~/.claude/settings.json` (sekce `env`).
- Kterýkoli náš model může fungovat (např. `qwen3-coder-next`), ale ne všechny
  garantovaně. Přestane-li Claude odpovídat → nejčastěji překročený **kontext**
  → přepni na model s větším oknem / zkrať text.

### Codex (OpenAI CLI)

```bash
export OPENAI_BASE_URL=https://llm.ai.e-infra.cz
export OPENAI_API_KEY=sk-...
codex --model coder --full-auto
# při přihlášení: "Provide your own API key"
```

### OpenCode

`~/.config/opencode/opencode.json` → provider `litellm`, baseURL
`https://llm.ai.e-infra.cz/v1`, modely `agentic/mini/glm/coder/thinker`.
Pak `opencode` → `/connect` → vyber **LiteLLM** → vlož API key → model `coder`.
(`gpt-oss-120b` jen částečná podpora.)

### Hermes (Nous Research)

AI coding agent; konfigurace stažitelná z dokumentace (config download →
`~/.hermes/config.yaml`). Autentizace: `OPENAI_API_KEY` = e-infra API key,
nebo klíč přímo v `config.yaml`.

### VS Code

- **Claude Code extension**: `@ext:Anthropic.claude-code` → Environment Variables →
  `claudeCode.environmentVariables` se stejnými `ANTHROPIC_*` proměnnými
  (API token do `ANTHROPIC_AUTH_TOKEN`), restart VS Code.
- **Continue / Zoo-Code**: provider `OpenAI Compatible`,
  Base URL `https://llm.ai.e-infra.cz/v1`, API key, model `coder` (nebo embedding
  model pro codebase indexing, např. `qwen3-embedding-4b`, dimenze `2560`,
  index do lokálního Qdrantu). (Roo Code už **není podporován** — nová verze
  rozšíření nefunguje s naším API.)
- Piš si vlastní **API key**, nikdy ho nepublikuj do configů, které jdou do gitu.

### JetBrains

- AI Assistant plugin → custom OpenAI-compatible provider (Base URL
  `https://llm.ai.e-infra.cz/v1`, model `coder`) — funguje **jen chat mód**.
- Pro agentní workflow použij Claude Code sekci výše.

## Pasti / tipy

- Non-streaming API requesty mají timeout 30 min (nekonfigurovatelné) — pro
  dlouhé běhy použij streaming.
- Tokeny spotřebované ve WebUI se **nepočítají** v usage dashboardu (jen API).
- API key nikdy nesdílej → okamžité blokování přístupu.
- Model status live: https://llm.ai.e-infra.cz/status/

## Související

- AI v Jupyteru (obrazy `...with AI`, Claude Code v notebooku, RStudio, VSCode) →
  `jupyterhub.md`.
- Referenční raw materiál: `raw/cerit/ai-as-a-service/`.
