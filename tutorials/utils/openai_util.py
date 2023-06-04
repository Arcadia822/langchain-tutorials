import os

import openai
from dotenv import load_dotenv


def init_openai():
    load_dotenv("../.env")

    openai.api_type = os.environ.get("OPENAI_API_TYPE")
    openai.api_version = os.environ.get("OPENAI_API_VERSION")
    openai.api_base = os.environ.get("OPENAI_API_BASE")
    openai.api_key = os.environ.get("OPENAI_API_KEY")


def init_openai_deploy():
    model = os.environ.get("OPENAI_MODEL")
    deployment_id = os.environ.get("OPENAI_DEPLOYMENT_ID")
    return model, deployment_id
