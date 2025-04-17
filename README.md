# 🔧 GitHub MCP Tool Server

This repo contains a lightweight [MCP (Model Context Protocol)](https://docs.anthropic.com/claude/docs/mcp-overview) server that exposes simple GitHub utilities — allowing AI applications like Cursor or Claude to interact with GitHub repositories.

### ✨ Features
- ✅ `get_repo_summary(repo_url)` — Fetches basic metadata of a GitHub repository
- ✅ `get_recent_commits(repo_url, count)` — Lists the most recent commits to a repo

---

## 🚀 Getting Started

### 📦 Requirements
- Python 3.10+
- [`uv`](https://github.com/astral-sh/uv) package manager *(recommended)*
- GitHub Personal Access Token (optional, but prevents rate limiting)

---

## ⚙️ Installation

```bash
# Clone the repo
git clone https://github.com/rajpanjabi/MCP.git
cd MCP

# Create virtual environment
uv venv .venv
source .venv/bin/activate

# Install dependencies
uv pip install httpx mcp
```

> 💡 Optionally, create a `.env` file or export your GitHub token:
```bash
export GITHUB_PAT=ghp_yourTokenHere
```

---

## 🛠️ Usage with MCP

You can run this server using:

```bash
uv run github_tool_mcp_server.py
```

It will launch in `stdio` mode and wait for tool calls via an MCP-compatible orchestrator like Claude Desktop or Cursor.

---

## 🖥️ Cursor Integration (Optional)

Add the following to your `cursor.config.json`:

```json
{
  "mcpServers": {
    "github": {
      "command": "uv",
      "args": [
        "--directory",
        "/absolute/path/to/your/project",
        "run",
        "github.py"
      ]
    }
  }
}
```

> Replace `/absolute/path/to/your/project` with your actual directory.

---

## 🧪 Example Tools

### 🔍 1. `get_repo_summary`

```json
{
  "name": "get_repo_summary",
  "arguments": {
    "repo_url": "https://github.com/username/repositoryname"
  }
}
```

**Output:**
```
**username/repositoryname**
Description: Lorem ipsum nhwjsrecv dweicdjv 
Stars: 10 | Forks: 2
Language: JavaScript | Open Issues: 1
Updated: 2024-11-22T18:22:33Z
```

---

### 🕵️ 2. `get_recent_commits`

```json
{
  "name": "get_recent_commits",
  "arguments": {
    "repo_url": "https://github.com/username/repositoryname",
    "count": 3
  }
}
```

**Output:**
```
[abc1234] by Raj: Added README structure
[def5678] by Raj: Fixed deployment config
[xyz9999] by Raj: Initial commit
```

---






