# AIM Hackathon March 2025 - Put News Archives to Life
Repository for the AIM Hackathon together with Media Innovation Lab on 22.03.2025

<br>


## Jump start
### Fork this repository
Simply fork this repository to start working on your project.

### Add data
Download data via the private link in the slack channel.

Place the `data` folder in this repository.

## Set up LLM API Keys
Copy your teams API key from the [slack]("TODO") channel description and place it in the `.env_template` file.

Don't forget to replace the filename to `.env` afterwards!

Check out the [sample code](notebooks/llm_rag_demo.ipynb) to see how to load the key.

You can also change the model in the `.env` file, see notes on available models [below](#change-model-to-use).

### Set up environment
With [uv](https://docs.astral.sh/uv/getting-started/installation/):
```bash
uv sync
```

With [conda](https://docs.conda.io/projects/conda/en/latest/user-guide/install/windows.html):
```bash
conda create -n aim_hackathon_oct24 python=3.13
pip install -r requirements.txt
```

### Sample code
There is a super simple RAG implementation to help getting you started: [llm_rag_demo.ipynb](notebooks/llm_rag_demo.ipynb).

<br>


## Hints

### For the challenge
Info Material:
- Basics of RAG [blog post](https://medium.com/@ahmed.mohiuddin.architecture/using-ai-to-chat-with-your-documents-leveraging-langchain-faiss-and-openai-3281acfcc4e9)
- Force LLMs to output e.g. only integers with [Structured outputs](https://platform.openai.com/docs/guides/structured-outputs/introduction) (highly recommended)
- Agentic AI introduction [blog post](https://www.anthropic.com/engineering/building-effective-agents)


Code samples:
- Sample notebook for this challenge (simple RAG pipeline): [llm_rag_demo.ipynb](notebooks/llm_rag_demo.ipynb) 
- RAG Techniques collection with sample code: [RAG Techniques GitHub](https://github.com/NirDiamant/RAG_Techniques)


### For token usage control
- *TODO* Ask us for current usage (easiest) 
- [Extract openAI API token usage](https://help.openai.com/en/articles/6614209-how-do-i-check-my-token-usage) from the response with `response['usage']`.
- Use [tiktoken](https://cookbook.openai.com/examples/how_to_count_tokens_with_tiktoken) to manually count tokens of a string:
```bash
import tiktoken
tokenizer = tiktoken.get_encoding("o200k_base")  # for gpt 4o
```

<br>

## Change model to use

Choose a model from OpenRouter's [model list](https://openrouter.ai/models) and place the model name in the `.env` file.

We recommend a model of these (click on the link to obtain code to run the model, scroll down):

| Name | MODEL_NAME                    | Cost | Comments    |
| --- |------------------------------------| --- |-------------|
| [OpenAI 4o](https://openrouter.ai/openai/gpt-4o) | `openai/gpt-4o`                    | 2.5$/M tokens | Recommended |
| [OpenAI 4o-mini](https://openrouter.ai/openai/gpt-4o-mini) | `openai/gpt-4o-mini`               | 0.15$/M tokens |          |
| [Google Gemini 2.0 Flash Lite](https://openrouter.ai/google/gemini-2.0-flash-lite-001) | `google/gemini-2.0-flash-lite-001` | 0.075$/M tokens |           |
| [Anthropic Claude 3.7 Sonnet](https://openrouter.ai/anthropic/claude-3.7-sonnet) | `anthropic/claude-3.7-sonnet`      | $3/M tokens |           |



Feel free to choose any model from these providers (advanced):
- OpenAI: https://openrouter.ai/provider/openai
- Google Vertex: https://openrouter.ai/provider/google-vertex
- Anthropic: https://openrouter.ai/provider/anthropic
- Mistral: https://openrouter.ai/provider/mistral
- Perplexity: https://openrouter.ai/perplexity
- Nebious: https://openrouter.ai/nebious (for deepseek R1, Qwen, Llama)