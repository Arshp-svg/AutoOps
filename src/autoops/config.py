from pathlib import Path
from dotenv import load_dotenv
import os

def load_env():
    """Load environment variables from .env file if it exists"""
    # Try to find .env in current working directory first
    env_paths = [
        Path.cwd() / ".env",  # Current working directory
        Path(__file__).parent.parent.parent / ".env",  # Project root (for dev)
        Path.home() / ".autoops" / ".env",  # User's home directory
    ]
    
    for env_path in env_paths:
        if env_path.exists():
            load_dotenv(dotenv_path=env_path, override=True)
            return
    
    # No .env file found - environment variables should be set by user

# Load immediately on import
load_env()

# Configuration with defaults
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
REPO_OWNER = os.getenv("REPO_OWNER")
REPO_NAME = os.getenv("REPO_NAME")
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
GROQ_MODEL = os.getenv("GROQ_MODEL", "llama3-70b-8192")

# Validation (optional - raises error if critical vars missing)
def validate_config():
    """Validate that required environment variables are set"""
    required_vars = {
        "GITHUB_TOKEN": GITHUB_TOKEN,
        "REPO_OWNER": REPO_OWNER,
        "REPO_NAME": REPO_NAME,
        "GROQ_API_KEY": GROQ_API_KEY,
    }
    
    missing = [key for key, value in required_vars.items() if not value]
    if missing:
        raise ValueError(
            f"Missing required environment variables: {', '.join(missing)}\n"
            f"Set them in your environment or create a .env file in your project directory."
        )