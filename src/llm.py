from langchain_openai import ChatOpenAI, AzureOpenAIEmbeddings
from langchain_google_genai.embeddings import GoogleGenerativeAIEmbeddings
import os

### Openrouter LLM completions
def get_llm_client(**kwargs):
    return ChatOpenAI(
        openai_api_key=os.getenv("OPENROUTER_API_KEY"),
        openai_api_base="https://openrouter.ai/api/v1",
        model_name=os.getenv("OPENROUTER_MODEL_NAME"),
        **kwargs
    )

### Azure OpenAI Embeddings
def get_azure_embeddings_client(**kwargs):
    return AzureOpenAIEmbeddings(
        azure_endpoint=os.getenv("AZURE_ENDPOINT"),
        openai_api_key=os.getenv("AZURE_OPENAI_API_KEY"),
        openai_api_version="2024-02-01",
        **kwargs
    )

### Google Gemini
# LLM completions
def get_gemini_llm_client(**kwargs):
    return ChatOpenAI(
        openai_api_key=os.getenv("GEMINI_API_KEY"),
        openai_api_base="https://generativelanguage.googleapis.com/v1beta/openai/",
        model_name=os.getenv("GEMINI_MODEL_NAME"),
        **kwargs
    )

# Embeddings
def get_gemini_embeddings_client():
    return GoogleGenerativeAIEmbeddings(
        google_api_key=os.getenv("GEMINI_API_KEY"),
        model="models/text-embedding-004",
    )
