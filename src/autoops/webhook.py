
import asyncio
from datetime import datetime
from .github import logs_downloader, github_api
from .ai_client import analyze_with_groq
from .utils.fileops import save_log
from .config import REPO_OWNER, REPO_NAME

async def handle_github_event(payload: dict):
    # minimal normalization
    workflow_run = payload.get("workflow_run") or payload.get("workflow") or payload
    conclusion = workflow_run.get("conclusion")
    head_branch = workflow_run.get("head_branch") or workflow_run.get("head_ref") or "unknown"
    run_id = workflow_run.get("id") or workflow_run.get("run_id") or int(datetime.utcnow().timestamp())
    # For demo, accept any event and analyze a sample log
    logs_text = logs_downloader.fetch_logs(run_id)
    save_log(f"ci_{run_id}.txt", logs_text)
    analysis = analyze_with_groq(logs_text)
    # create an issue summarizing the analysis
    issue_url = github_api.create_issue(f"[AutoOps] CI failure analysis ({head_branch})", analysis)
    return {"status": "processed", "issue": issue_url, "analysis_preview": analysis[:500]}
