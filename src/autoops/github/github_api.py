
import requests
from ..config import GITHUB_TOKEN, REPO_OWNER, REPO_NAME

BASE = "https://api.github.com"
HEADERS = {"Authorization": f"token {GITHUB_TOKEN}", "Accept": "application/vnd.github.v3+json"} if GITHUB_TOKEN else {}

def create_issue(title, body):
    if not GITHUB_TOKEN:
        return None
    url = f"{BASE}/repos/{REPO_OWNER}/{REPO_NAME}/issues"
    payload = {"title": title, "body": body}
    r = requests.post(url, json=payload, headers=HEADERS)
    try:
        r.raise_for_status()
        return r.json().get("html_url")
    except Exception as e:
        return f"Failed to create issue: {e} - {r.text if r is not None else ''}"
