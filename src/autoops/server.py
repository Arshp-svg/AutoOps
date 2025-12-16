
from fastapi import FastAPI, Request, HTTPException
from .webhook import handle_github_event
app = FastAPI(title="AutoOps Server (Groq)")

@app.get("/")
async def root():
    return {"status": "AutoOps (Groq) running"}

@app.post("/webhook/github")
async def github_webhook(request: Request):
    try:
        payload = await request.json()
    except Exception:
        raise HTTPException(status_code=400, detail="invalid json")
    result = await handle_github_event(payload)
    return result
