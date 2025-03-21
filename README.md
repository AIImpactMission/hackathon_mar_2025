# AIM Hackathon March 2025 - Getting started
Repository for the AIM Hackathon "Put News Archives to Life" together with Media Innovation Lab on Sa, 22.03.2025

> Note: This repository should make the start easier for you, but is not mandatory to use - feel free to use your own setup!

> If you get stuck, feel free to call us in the slack channel any time! :)


## 1) Fork this repository
Simply fork this repository to start working on your project.



## 2) Set up environment
### With `uv` 
recommended, [installation guide](https://docs.astral.sh/uv/getting-started/installation/) <br>
-> no conda or other environment required, very easy to use and super fast
```bash
uv sync
```

Optional: Install new packages similar to pip:
```bash
uv pip install <package>
```


### With [conda](https://docs.conda.io/projects/conda/en/latest/user-guide/install/windows.html)
```bash
conda create -n aim_hackathon_oct24 python=3.13
pip install -r requirements.txt
```



## 3) Set up API keys
Copy your teams API key from the [slack]("TODO") channel description and place it in the `.env_template` file.

Don't forget to replace the filename to `.env` afterwards!

Check out the [sample code](notebooks/getting_started_llms.ipynb) to see how to load the key.

Check out pricing on the OpenRouter model pages (see [below](#change-model-to-use))

*TODO*: Maybe update with OpenRouter overview?

<br>


## 4) Add data
Download data via the private link in the slack channel.

Place the downloaded zip in this repository.

Unzip the data:
```bash
unzip data.zip
```


The folder contains:
- articles_clean: the cleaned articles (using [this script](notebooks/dataset.ipynb)) in json format
- `metadata.csv`: metadata for the articles, including tags for topics created with zero-shot models (using [this script](notebooks/metadata.ipynb))

> Note: Take the assigned tags with a grain of salt, they are not perfect as they are automatically created.

<br>


## 5) Get started with developing
- Collect ideas, goals and approaches
- Check out and filter the data with [filter_dataset.ipynb](notebooks/filter_dataset.ipynb)
- Once you created a subset, there is a simple RAG implementation to help you getting started: [getting_started_llms.ipynb](notebooks/getting_started_llms.ipynb).

> Note: Feel free to diverge from this approach! This is just a starting point.

<br>


## Hints

### For the challenge
Info Material:
- Basics of RAG [blog post](https://medium.com/@ahmed.mohiuddin.architecture/using-ai-to-chat-with-your-documents-leveraging-langchain-faiss-and-openai-3281acfcc4e9)
- RAG techniques and sample code [here]()
- Force LLMs to output e.g. only integers with [Structured outputs](https://platform.openai.com/docs/guides/structured-outputs/introduction) (highly recommended)
- Agentic AI introduction [blog post](https://www.anthropic.com/engineering/building-effective-agents)
- Prompt caching to reduce token usage [blog post](https://platform.openai.com/docs/guides/prompt-caching)


Code samples:
- Getting started notebook for this challenge (simple RAG pipeline): [llm_rag_demo.ipynb](notebooks/getting_started_llms.ipynb) 
- RAG Techniques collection with sample code: [RAG Techniques GitHub](https://github.com/NirDiamant/RAG_Techniques)


### For token usage control (advanced)
- *TODO* Ask us for current usage (easiest) 
- [Extract openAI API token usage](https://help.openai.com/en/articles/6614209-how-do-i-check-my-token-usage) from the response with `response['usage']`.
- Use [tiktoken](https://cookbook.openai.com/examples/how_to_count_tokens_with_tiktoken) to manually count tokens of a string:
```bash
import tiktoken
tokenizer = tiktoken.get_encoding("o200k_base")  # for gpt 4o
```

<br>

## Change model to use (advanced)

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


