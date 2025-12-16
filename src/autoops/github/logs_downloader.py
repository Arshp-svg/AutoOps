
import requests
from ..config import GITHUB_TOKEN, REPO_OWNER, REPO_NAME

BASE = "https://api.github.com"

def fetch_logs(run_id):
    # Lightweight metadata fetch: in production, download logs_url and extract zipped logs.
    if not (GITHUB_TOKEN and REPO_OWNER and REPO_NAME):
        return f"DEBUG: missing GITHUB_TOKEN/REPO info. run_id={run_id}"
    headers = {"Authorization": f"token {GITHUB_TOKEN}", "Accept": "application/vnd.github.v3+json"}
    try:
        r = requests.get(f"{BASE}/repos/{REPO_OWNER}/{REPO_NAME}/actions/runs/{run_id}", headers=headers, timeout=10)
        r.raise_for_status()
        data = r.json()
        return f"Fetched workflow run metadata for {run_id}: {data.get('conclusion')}\nlogs_url: {data.get('logs_url')}\n\nFull metadata:\n{data}"
    except Exception as e:
        return f"Failed to fetch run metadata: {e}"
