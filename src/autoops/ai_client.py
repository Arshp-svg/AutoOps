
"""Groq client wrapper for simple chat/text completions."""
import os
from typing import Optional

# Prefer using Groq Python SDK when available.
try:
    # groq Python SDK exposes easy chat interfaces (see Groq docs).
    from groq.cloud.core import ChatCompletion
    SDK_AVAILABLE = True
except Exception:
    SDK_AVAILABLE = False

import requests
from .config import GROQ_API_KEY, GROQ_MODEL

def analyze_with_groq(text: str, model: Optional[str] = None) -> str:
    model = model or GROQ_MODEL or "llama2-70b-4096"
    prompt = f"""You are an expert DevOps engineer. Analyze the following CI logs and provide a concise structured analysis including:\n1) error_category\n2) explanation\n3) likely_files\n4) suggested_fix (step list)\n\nLogs:\n{text[:15000]}\n"""

    if SDK_AVAILABLE:
        # Example using the Groq SDK ChatCompletion helper.
        try:
            with ChatCompletion(model) as chat:
                response, _, _ = chat.send_chat(prompt)
                return response
        except Exception as e:
            # fallback to HTTP API
            return _analyze_via_http(prompt, model, str(e))

    return _analyze_via_http(prompt, model, None)


def _analyze_via_http(prompt: str, model: str, sdk_error: Optional[str] = None) -> str:
    """Fallback HTTP call to Groq's OpenAI-compatible endpoint.
    This uses the Groq OpenAI-compatible API path. Check Groq docs for the most up-to-date endpoint.
"""
    if not GROQ_API_KEY:
        return "GROQ_API_KEY not configured. Set environment variable GROQ_API_KEY."

    url = "https://api.groq.com/openai/v1/chat/completions"
    headers = {"Authorization": f"Bearer {GROQ_API_KEY}", "Content-Type": "application/json"}
    payload = {
        "model": model,
        "messages": [{"role": "user", "content": prompt}],
        "max_output_tokens": 800
    }
    try:
        r = requests.post(url, json=payload, headers=headers, timeout=30)
        r.raise_for_status()
        data = r.json()
        # Groq's OpenAI-compatible responses often include structure similar to openai responses.
        # Try to extract text.
        if "choices" in data and len(data["choices"])>0:
            choice = data["choices"][0]
            # Some Groq responses put text under 'message' or 'text' fields
            if "message" in choice and "content" in choice["message"]:
                return choice["message"]["content"]
            if "text" in choice:
                return choice["text"]
            if "message" in choice and isinstance(choice["message"], dict):
                return str(choice["message"]) 
        # If structured differently, return raw json for debugging
        return f"SDK error: {sdk_error}\nRaw response: {data}"
    except Exception as e:
        return f"Error calling Groq API: {e}"
