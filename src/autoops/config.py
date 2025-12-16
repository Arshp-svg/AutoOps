from pathlib import Path
from dotenv import load_dotenv
import os

ENV_PATH = Path(".env")


def load_env():
    if ENV_PATH.exists():
        load_dotenv(dotenv_path=ENV_PATH)


# Load .env immediately on import
load_env()

GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
REPO_OWNER = os.getenv("REPO_OWNER")
REPO_NAME = os.getenv("REPO_NAME")
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
GROQ_MODEL = os.getenv("GROQ_MODEL", "llama2-70b-4096")
