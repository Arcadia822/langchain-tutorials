from os import environ as env

import openai
from dotenv import load_dotenv
from langchain.chat_models import AzureChatOpenAI, ChatOpenAI
from langchain.chat_models.base import BaseChatModel


def init_openai():
    api_key = env.get("OPENAI_API_KEY")

    if not api_key:
        raise ValueError("OPENAI_API_KEY not set.")

    openai.api_key = api_key
    openai.api_type = env.get("OPENAI_API_TYPE")
    openai.api_version = env.get("OPENAI_API_VERSION")
    openai.api_base = env.get("OPENAI_API_BASE")


def init_chat_model(dotenv_path=None) -> BaseChatModel:
    """Initialize the chat model. load environment variables and return the model."""
    """You can pass a dotenv file to load environment variable from."""

    if dotenv_path:
        load_dotenv(dotenv_path)

    model_type = env.get("API_TYPE", "openai")
    if model_type != "openai":
        raise NotImplementedError(f"Only openai is supported. Got {model_type}.")

    init_openai()

    openai_api_type = env.get("OPENAI_API_TYPE")
    if not openai_api_type:
        model = ChatOpenAI()
        return model

    if openai_api_type == "azure":
        model = env.get("OPENAI_MODEL")
        deployment_id = env.get("OPENAI_DEPLOYMENT_ID")

        model = AzureChatOpenAI(model=model, deployment_name=deployment_id)
        return model


if __name__ == "__main__":
    llm = init_chat_model("../../.env")
    print(llm.call_as_llm("Hello!"))
