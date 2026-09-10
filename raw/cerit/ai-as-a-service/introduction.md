#

## [AI for Science. Built for Researchers. Run securely in e-INFRA CZ.](#ai-for-science-built-for-researchers-run-securely-in-e-infra-cz)

CERIT‑SC, a core component of e‑INFRA CZ, operates an **on‑premise AI platform** that provides researchers with secure, high‑performance, and interoperable AI tools. This platform runs on cutting‑edge NVIDIA DGX‑H100/B200/B300‑class systems, delivering robust computational power for high‑speed inference. The environment hosts open large language and generative models, accessible via the [Open WebUI interface](../ai-as-a-service/chat-ai) or standard [OpenAI‑compatible APIs](../ai-as-a-service/ai-api).

**New: Matrix Community Channel** — [Matrix](../web-apps/matrix) is now available for LLM service users to share knowledge and best practices, exchange experiences, and stay up to date with service status.

### [Key Features (Inference)](#key-features-inference)

- **Secure, on‑premise LLM & generative‑AI platform** – Our models run securely on the e‑INFRA CZ infrastructure. Queries and responses are not logged by external providers, ensuring that your research and sensitive data remain within our environment. With the exception of internet searching, nothing leaves our local infrastructure.

- **Supports privacy‑sensitive research** – compliance with institutional and legal requirements. This makes our services ideal for handling sensitive data.

For more details, see [AI Data privacy section](../ai-as-a-service/ai-data-privacy)

### [What the Platform Provides](#what-the-platform-provides)

| Category |Highlights |
| **Compute** |**NVIDIA DGX‑H100/B200/B300**. Petaflop‑class GPU performance. |
| **Key Models** |
 Our portfolio includes advanced models tailored for programming, image generation, code generation, tool use, and agentic workflows. Featured models include Kimi, GLM, DeepSeek, Qwen,… For enhanced security, these models operate entirely offline without internet access [View other available models](../ai-as-a-service/chat-ai#currently-available-models)


[Model status page](https://llm.ai.e-infra.cz/status/)


[API token personal usage](https://llm.ai.e-infra.cz/usage)

 |
| **Models’ Metadata** |You can retrieve [models’ metadata](../ai-as-a-service/ai-api#getting-model-metadata-via-the-api) through the /model/info endpoint. |
| **Access** |MUNI students and employees and MetaCentrum users |

### [Key AI Services (Inference)](#key-ai-services-inference)

| Service |Link |Description |
| **Chat (Open‑WebUI)** |[WebUI chat](../ai-as-a-service/chat-ai) |
A full‑featured conversational interface (similar to ChatGPT) offering advanced features and explicit language model selection.


 **Text Work**: Translations, summaries, analysis, and generation of program code.


**Multimodality**: Image generation (including editing) and content recognition in images (e.g., extracting a serial number from a photo).


**Tools**: Searching the internet, GitHub, arXiv, and a Python sandbox for running code in the browser and data analytics.


**RAG (Knowledge)**: Searching within a document attached to the chat works very well.

 |
| **OpenAI-compatible API** |[OpenAI API](../ai-as-a-service/ai-api) |Use the OpenAI‑compatible endpoint to integrate AI into your scripts, pipelines, or services. |
| **MCP servers** |[MCP servers](../ai-as-a-service/mcp) |We provide several MCP servers that are available through the [https://llm.ai.e-infra.cz](https://llm.ai.e-infra.cz) API. A particular MCP server is available at [https://llm.ai.e-infra.cz/[servername]/mcp](https://llm.ai.e-infra.cz/%5Bservername%5D/mcp). |
| **AI Coding Assistants** |[AI Coding Assistants Integration](../ai-as-a-service/llm-integration) |By connecting your tools to our backend, you can leverage high‑performance models for coding tasks (ClaudeCode, OpenCode, VSCode,… support. |
| **DeepSite** |[DeepSite (vibe‑coding)](../ai-as-a-service/deepsite) |A generative tool that creates webpages and applications (HTML/CSS/JS) based on a simple text description. Excellent for design proposals, mockups, or quick web concepts. |
| **AI in Jupyter Notebooks** |[JupyterHub integration](../web-apps/jupyterhub) |Integration of an AI Assistant directly into the Jupyter Lab environment Notebook Intelligence). Used for fixing code (R or Python), generating new snippets, and conversational assistance within your coding projects. |
| **n8n platform** |[n8n Agents](../ai-as-a-service/n8n-agents) |n8n is an open‑source, low‑code workflow automation platform with AI Agent functionality |
| **DeepSec vulnerability scanner** |[DeepSec](../ai-as-a-service/deepsec) |AI-powered vulnerability scanner designed to run in your own infrastructure. It performs on-demand security reviews of entire codebases — including large-scale repositories — by combining fast regex-based candidate detection with deep AI investigation. |
| **Documentation ChatBot** |docs.e-infra.cz and other documentation sites |A Retrieval‑Augmented Generation (RAG) system implemented across e‑INFRA CZ documentation. Answers specific questions and acts as a problem solver based on our knowledge base (e.g., “How to run MATLAB?”). |
| **Matrix Discussion Channel** |[Matrix](../web-apps/matrix) |Real-time chat for LLM service users to ask questions, share knowledge, and stay updated. |

## [Reference](#reference)

Read more details on our e‑INFRA Blog at [https://blog.e-infra.cz/](https://blog.e-infra.cz/)

![publicity banner](/_next/static/media/einfra_cerit-zapati.04hjcx2t12mah.svg)

### On this page
[AI for Science. Built for Researchers. Run securely in e-INFRA CZ.](#ai-for-science-built-for-researchers-run-securely-in-e-infra-cz)[Key Features (Inference)](#key-features-inference)[What the Platform Provides](#what-the-platform-provides)[Key AI Services (Inference)](#key-ai-services-inference)[Reference](#reference)

![einfra banner](/_next/image?url=%2F_next%2Fstatic%2Fmedia%2Fheader03.0ikyctvi6x5ki.png&w=384&q=75)
