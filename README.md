🚀 AutoOps

AutoOps is a fully automatic AI DevOps agent that monitors GitHub Actions failures and creates GitHub issues with AI-generated root-cause analysis and fix suggestions.

👉 One command. Zero setup. Fully automatic.

```
autoops run
```

✨ Features

- 🤖 AI-powered CI/CD failure analysis
- 🔁 Automatic GitHub Actions polling (no webhooks)
- 📌 Auto-creates GitHub issues on failure
- ⚙️ One-command usage
- 🔐 Simple .env configuration
- 🧠 Groq-powered LLM analysis

📦 Installation

```
pip install autoops
```

⚙️ Configuration

Create a `.env` file in your repository root:

```
GITHUB_TOKEN=ghp_xxx
REPO_OWNER=your-github-username
REPO_NAME=your-repository-name
GROQ_API_KEY=groq_xxx
```

🔐 Your GitHub token must have `repo` and `workflow` permissions.

▶️ Usage

Run AutoOps:

```
autoops run
```

That’s it.

AutoOps will:

- Poll GitHub Actions
- Detect failed workflows
- Analyze failures using AI
- Create GitHub issues automatically

🔁 Upgrade Notes (IMPORTANT)

🚨 Breaking change in v0.2.0

If you are upgrading from v0.1.x:

- ❌ `autoops setup` has been removed
- ❌ Webhooks / ngrok are no longer required

✅ New behavior (v0.2.0+)

- Configuration is now via `.env`
- AutoOps runs in polling mode
- One command only: `autoops run`

This change makes AutoOps:

- Simpler to use
- Fully automatic
- More production-friendly

🧠 How it works (High level)

```
AutoOps → GitHub Actions API → AI Analysis → GitHub Issue
```

No inbound connections required.

🛠️ Roadmap

- 🔄 Multi-repo support
- 🧪 Smarter log extraction
- 🔧 Auto-fix PR generation
- 📣 Slack / Teams notifications
- 🐳 Docker & cloud deployment

