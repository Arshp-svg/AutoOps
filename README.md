
# AutoOps - AI DevOps Agent (Groq)

AutoOps is an AI DevOps Agent that monitors GitHub workflow events, analyzes CI failures, and proposes fixes.
This scaffold uses **Groq (Groq Cloud)** as the AI backend instead of OpenAI.

Quick start:
```bash
pip install -r requirements.txt
export GROQ_API_KEY=your_groq_api_key
export GROQ_MODEL=your_model_id   # e.g. mixtral-8x7b or llama2-70b-4096 depending on your Groq account
autoops setup
autoops run --port 8000
# in another terminal
autoops test --port 8000
```

Notes:
- The Groq Python SDK is used (`pip install groq`). See Groq docs: https://console.groq.com/docs/ and https://github.com/groq/groq-python for more details.
