from typing import Optional
import httpx
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("github_tools")

GITHUB_API_BASE = "https://api.github.com"
HEADERS = {
    "Accept": "application/vnd.github+json",
    "User-Agent": "mcp-github-tool/0.1"
}

async def fetch_json(url: str) -> dict:
    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(url, headers=HEADERS)
            response.raise_for_status()
            return response.json()
        except Exception as e:
            return {"error": str(e)}

@mcp.tool()
async def get_repo_summary(repo_url: str) -> str:
    """Get a summary of a GitHub repository."""
    try:
        owner_repo = repo_url.strip("/").split("github.com/")[-1]
        url = f"{GITHUB_API_BASE}/repos/{owner_repo}"
        data = await fetch_json(url)

        if "error" in data:
            return f"Error fetching repo: {data['error']}"

        return (
            f"**{data['full_name']}**\n"
            f"Description: {data['description']}\n"
            f"Stars: {data['stargazers_count']} | Forks: {data['forks_count']}\n"
            f"Language: {data['language']} | Open Issues: {data['open_issues_count']}\n"
            f"Updated: {data['updated_at']}"
        )
    except Exception as e:
        return f"Exception: {e}"

@mcp.tool()
async def get_recent_commits(repo_url: str, count: int = 3) -> str:
    """Get the most recent commits for a GitHub repo."""
    try:
        owner_repo = repo_url.strip("/").split("github.com/")[-1]
        url = f"{GITHUB_API_BASE}/repos/{owner_repo}/commits"
        commits = await fetch_json(url)

        if "error" in commits:
            return f"Error fetching commits: {commits['error']}"

        messages = []
        for c in commits[:count]:
            commit_msg = c['commit']['message'].split("\n")[0]
            sha = c['sha'][:7]
            author = c['commit']['author']['name']
            messages.append(f"[{sha}] by {author}: {commit_msg}")

        return "\n".join(messages)
    except Exception as e:
        return f"Exception: {e}"

if __name__ == "__main__":
    mcp.run(transport="stdio")
