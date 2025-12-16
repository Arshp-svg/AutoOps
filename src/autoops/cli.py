
import typer
import subprocess
import json
import requests
from pathlib import Path
from .config import load_env, ENV_PATH
load_env()

app = typer.Typer(add_completion=False)

@app.command()
def setup():
    """Interactive setup to create a .env file in the current working directory."""
    cwd = Path.cwd()
    env_path = cwd / ".env"
    if env_path.exists():
        if not typer.confirm(".env already exists — overwrite?"):
            raise typer.Abort()
    gh = typer.prompt("GITHUB_TOKEN", default="")
    owner = typer.prompt("REPO_OWNER", default="")
    repo = typer.prompt("REPO_NAME", default="")
    groq_key = typer.prompt("GROQ_API_KEY", default="")
    groq_model = typer.prompt("GROQ_MODEL", default="")
    content = f"GITHUB_TOKEN={gh}\nREPO_OWNER={owner}\nREPO_NAME={repo}\nGROQ_API_KEY={groq_key}\nGROQ_MODEL={groq_model}\n"
    env_path.write_text(content, encoding="utf-8")
    typer.echo(f"Wrote {env_path}")


@app.command()
def run(host: str = "0.0.0.0", port: int = 8000):
    """Run the FastAPI app via uvicorn."""
    typer.echo(f"Starting AutoOps server on {host}:{port}")
    subprocess.run(["uvicorn", "autoops.server:app", "--host", host, "--port", str(port)], check=True)


@app.command()
def expose(port: int = 8000):
    """Expose local server using ngrok (requires ngrok on PATH)."""
    typer.echo("Starting ngrok tunnel...")
    try:
        subprocess.run(["ngrok", "http", str(port)], check=True)
    except FileNotFoundError:
        typer.echo("ngrok not found. Install from https://ngrok.com/")


@app.command()
def test(port: int = 8000):
    """Send a fake GitHub push event to validate webhook setup."""
    url = f"http://localhost:{port}/webhook/github"
    fake_event = {
        "zen": "Keep it logically awesome.",
        "hook_id": 123456,
        "repository": {"name": "autoops-test-repo", "full_name": "test/autoops-test-repo"},
        "pusher": {"name": "autoops-user"},
        "ref": "refs/heads/main",
        "head_commit": {"id": "test123", "message": "AutoOps test commit"},
    }
    headers = {"Content-Type": "application/json", "X-GitHub-Event": "push"}
    try:
        r = requests.post(url, json=fake_event, headers=headers, timeout=5)
        typer.echo(f"Status: {r.status_code}")
        typer.echo(r.text)
    except Exception as e:
        typer.echo("Error connecting to server: " + str(e))
