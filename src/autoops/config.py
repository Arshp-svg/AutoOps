
import os
from dotenv import load_dotenv
from pathlib import Path

# load .env from current working directory if present
ENV_PATH = Path.cwd() / ".env"
if ENV_PATH.exists():
    load_dotenv(dotenv_path=ENV_PATH)

GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
REPO_OWNER = os.getenv("REPO_OWNER")
REPO_NAME = os.getenv("REPO_NAME")
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
GROQ_MODEL = os.getenv("GROQ_MODEL", "llama2-70b-4096")
