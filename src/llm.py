from openai import OpenAI

from langchain_openai import ChatOpenAI
from langchain_google_genai.embeddings import GoogleGenerativeAIEmbeddings
import os

def get_llm_client(**kwargs):
    return ChatOpenAI(
        openai_api_key=os.getenv("OPENROUTER_API_KEY"),
        openai_api_base="https://openrouter.ai/api/v1",
        model_name=os.getenv("MODEL_NAME"),
        **kwargs
    )

def get_gemini_llm_client(**kwargs):
    return ChatOpenAI(
        openai_api_key=os.getenv("GEMINI_API_KEY"),
        openai_api_base="https://generativelanguage.googleapis.com/v1beta/openai/",
        model_name=os.getenv("MODEL_NAME"),
        **kwargs
    )

def get_gemini_embeddings_client():
    return GoogleGenerativeAIEmbeddings(
        google_api_key=os.getenv("OPENAI_API_KEY"),
        model="models/text-embedding-004",
    )

def get_openrouter_client(**kwargs):
    return OpenAI(
        base_url="https://openrouter.ai/api/v1",
        api_key=os.getenv("OPENROUTER_API_KEY"),
    )