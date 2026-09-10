#

## [API Introduction](#api-introduction)

This documentation provides detailed instructions for generating and using **API keys** to access locally running Large Language Models (LLMs) on the e-INFRA CZ infrastructure, specifically through the Open WebUI interface [https://chat.ai.e-infra.cz](https://chat.ai.e-infra.cz). The guide is designed for researchers and scientists who want to integrate these models into their applications, scripts, or AI workflows via API.

To access the Open WebUI service and generate an API key, you must meet the following prerequisites:

- A valid MetaCentrum account (for Czech research institutions)

- Or an active Masaryk University account (if affiliated).

For a comprehensive description of available models, see the [Chat AI documentation](../ai-as-a-service/chat-ai).

## [Creating an API Key](#creating-an-api-key)

Do not share the API key with other persons. Sharing API keys poses significant security risks and directly violates the user terms and conditions. If unauthorized sharing or misuse is detected, the associated API access may be immediately blocked.

API keys serve as authentication tokens to securely access Open WebUI’s API endpoint. Follow these steps to generate and use your API key:

**Step-by-Step Instructions**

- Go to the Settings section of the Open WebUI interface [https://chat.ai.e-infra.cz](https://chat.ai.e-infra.cz).

- Navigate to the Account (Účet).

- Click on API keys (display).

- Ignore JWT token, select API key, and either generate a new one or display the existing one.

- Copy the generated API key and store it securely.

- Use this key in API requests to authenticate and access Open WebUI services.

- The base endpoint for the Open-WebUI API is: `https://llm.ai.e-infra.cz/v1/`. This endpoint follows the OpenAI API specification, enabling compatibility with many existing LLM frameworks and applications.

## [Using the API Key](#using-the-api-key)

For detailed API specifications, refer to the [API reference](https://developers.openai.com/api/reference/overview). Note that not all endpoints are supported.

For client access and development, we recommend using either the [LiteLLM SDK](https://docs.litellm.ai/docs/#litellm-python-sdk) or the [OpenAI Client Libraries](https://developers.openai.com/api/docs/libraries/), which provide well-maintained, production-ready integrations.

User can monitor LLM token consumption directly via a new personal dashboard at [llm.ai.e-infra.cz/usage](https://llm.ai.e-infra.cz/usage).

- Available after logging in with your `e-INFRA CZ account`.

- The dashboard monitors tokens consumed exclusively through the **API endpoint**.

Note: Tokens generated via the WebUI are not tracked here.

### [Listing Available Models](#listing-available-models)

[Currently available models](/docs/ai-as-a-service/chat-ai#currently-available-models)

The up‑to‑date status of all currently available models is displayed at [https://llm.ai.e-infra.cz/status/](https://llm.ai.e-infra.cz/status/)

Before querying a model, ensure you use the correct model name. To retrieve a list of all available models on the e-INFRA CZ infrastructure, run the following using `curl` and `jq` commands.
Replace `${E_INFRA_API_TOKEN}` with your actual token.

```
curl -H "Authorization: Bearer ${E_INFRA_API_TOKEN}" https://llm.ai.e-infra.cz/v1/models | jq .data[].id

```

Expected Output (example):

```
"llama3.3:latest"
"llama3.3:70b-instruct-fp16"
"deepseek-r1:32b-qwen-distill-fp16"
"qwen2.5-coder:32b-instruct-q8_0"
"aya-expanse:latest"

```

This list reflects the model identifiers (`id`) that can be queried via the API. The identifiers follow a naming convention, typically including:

- The model name (e.g., `llama3.3`, `qwen2.5-coder`).

- A quantization tag (e.g., `fp16`, `q8_0`) that indicates how the model is optimized for inference (important for performance and resource consumption).

- A variant or revision (e.g., `:latest`, `:70b-instruct-fp16`).

### [Example API Request](#example-api-request)

Below is an example of how to use the API key to query the LLaMA 3.3 model (`llama3.3:latest`) with a chat completions request:

```
curl https://llm.ai.e-infra.cz/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer ${E_INFRA_API_TOKEN}" \
  -d '{
    "model": "mini",
    "messages": [
      {
        "role": "user",
        "content": "Explain the impact of machine learning on climate research in 100 words or less."
      }
    ]
  }'

```

Expected Output (example):

```
{
  "id": "chatcmpl-XYZ123",
  "object": "chat.completion",
  "model": "mini",
  "choices": [
    {
      "message": {
        "role": "assistant",
        "content": "Machine learning (ML) is revolutionizing climate research by unlocking unprecedented insights..."
      },
      "index": 0,
      "finish_reason": "length"
    }
  ]
}

```

## [Framework Integration](#framework-integration)

The e-INFRA CZ LLM API is designed to be compatible with the OpenAI API specification, meaning it can be integrated into frameworks originally built for OpenAI’s services.

### [Recommended approach for MCP servers](#recommended-approach-for-mcp-servers)

For requests sent from an MCP server, we recommend setting the `"stream": true` flag so that the gateway continuously sends SSE response chunks as the model generates and thereby keeps the connection active. The MCP server can append the individual chunks to a buffer and return one complete response to its client after the stream ends.

We recommend streaming requests from MCP servers

If this approach is not followed, the request may end with an HTTP `408` error regardless of the timeout configured in the MCP client or server. The e-INFRA infrastructure timeout for non-streaming calls is 30 minutes and cannot be overridden by application settings.

Recommended sequence:

- The MCP server sends the chat completions request with the `"stream": true` flag.

- As the model generates, the gateway continuously sends small SSE response chunks such as `…the`, ` filter`, and ` protects…`.

- The MCP server reads each chunk immediately and appends it to a buffer. The continuous flow of data keeps the connection active.

- When the stream ends, the server assembles the same complete object as for a non-streaming call — the answer text, model, `stop_reason`, `usage`, and any `thinking` content.

- It returns the assembled object to the MCP client once.

The MCP server therefore processes the SSE stream continuously on its connection to the e-INFRA CZ LLM API, while preserving its existing client-facing interface and returning only the final complete object.

**PyDanticAI Integration Example**

PyDanticAI is a framework that simplifies LLM interactions using OpenAI-compatible models. Use the following configuration to authenticate with the e-INFRA CZ LLM endpoint:

Example `PydanticAI` configuration for integrating with our API (use similar settings for other frameworks):

```
from pydantic_ai_provider import OpenAIModel, OpenAIProvider
import os

model = OpenAIModel(
    'deepseek',
    provider=OpenAIProvider(
        base_url="https://llm.ai.e-infra.cz/v1",
        api_key=os.getenv("E_INFRA_API_TOKEN"),
    ),
)

```

Beyond PyDanticAI, similar configurations can be applied to:

- LangChain

- LlamaIndex

- FastAPI-based applications

- Any other frameworks or clients that support OpenAI API custom endpoints.

## [Reasoning Models in the API](#reasoning-models-in-the-api)

Some models are **hybrid**, supporting both *reasoning (thinking)* and *non-reasoning* modes.

In the chat UI, most hybrid models are preconfigured to run in reasoning mode, which means you may see intermediate `thinking` output before the final response is returned. In the API, however, the default behavior depends on the specific model.

### [DeepSeek](#deepseek)

By default, **DeepSeek** runs *without* reasoning enabled. To enable reasoning, pass additional parameters via `chat_template_kwargs`:

```
curl https://llm.ai.e-infra.cz/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer xxx" \
  -d '{
    "model": "deepseek",
    "messages": [
      {
        "role": "user",
        "content": "What are 5 creative things I could do with my kids'' art? I don''t want to throw them away, but it''s also so much clutter."
      }
    ],
    "chat_template_kwargs": {
      "thinking": true
    }
  }'

```

For convenience—and for environments where `chat_template_kwargs` cannot be used (for example, certain AI agents)—we also provide a dedicated reasoning variant named **`deepseek-thinking`**, which is permanently forced into thinking mode.

Use these options to control whether intermediate reasoning is included in API responses, depending on your application’s needs.

## [Getting Model Metadata via the API](#getting-model-metadata-via-the-api)

You can retrieve metadata about all available models through the /model/info endpoint. This includes details such as model name, capabilities, context size, source, and quantization.

**Request Example**

```
curl --location 'https://llm.ai.e-infra.cz/v1/model/info' --header 'Content-Type: application/json' --header 'Accept: application/json, text/event-stream' --header 'x-litellm-api-key: Bearer TOKEN'  | jq '[.data[] | {model_name, capabilities: .model_info.capabilities, context_size: .model_info.context_size, model_source: .model_info.model_source, quantization: .model_info.quantization}]'

```

**Response Example**

The response is a JSON array containing metadata for each model.

```
{
    "model_name": "kimi-k2.6",
    "capabilities": [
      "chat",
      "multimodal",
      "tools"
    ],
    "context_size": 262144,
    "model_source": "https://huggingface.co/moonshotai/Kimi-K2.6",
    "quantization": "int4"
  },
  {
    "model_name": "gpt-oss-120b",
    "capabilities": [
      "chat",
      "tools"
    ],
    "context_size": 131072,
    "model_source": "https://huggingface.co/openai/gpt-oss-120b",
    "quantization": "mxfp4"
  },
  {
    "model_name": "gpt-oss-120b",
    "capabilities": [
      "chat",
      "tools"
    ],
    "context_size": 131072,
    "model_source": "https://huggingface.co/openai/gpt-oss-120b",
    "quantization": "mxfp4"
  }

```

![publicity banner](/_next/static/media/einfra_cerit-zapati.04hjcx2t12mah.svg)

### On this page
[API Introduction](#api-introduction)[Creating an API Key](#creating-an-api-key)[Using the API Key](#using-the-api-key)[Listing Available Models](#listing-available-models)[Example API Request](#example-api-request)[Framework Integration](#framework-integration)[Recommended approach for MCP servers](#recommended-approach-for-mcp-servers)[Reasoning Models in the API](#reasoning-models-in-the-api)[DeepSeek](#deepseek)[Getting Model Metadata via the API](#getting-model-metadata-via-the-api)

![einfra banner](/_next/image?url=%2F_next%2Fstatic%2Fmedia%2Fheader03.0ikyctvi6x5ki.png&w=384&q=75)
