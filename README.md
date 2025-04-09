# Metricool MCP Server

This is a Multi-Agent Collaboration Protocol (MCP) server for interacting with the Metricool API. It allows AI agents to access and analyze social media metrics and campaign data from your Metricool account.

## Setup

### Prerequisites

- Python 3.8 or higher
- A Metricool account with API access (Advanced Tier)
- Required environment variables set up

### Configuration
1. Configure Claude Desktop
Create the following file depending on your OS:

On MacOS: ~/Library/Application Support/Claude/claude_desktop_config.json

On Windows: %APPDATA%/Claude/claude_desktop_config.json

Paste this template in the file and replace <METRICOOL_USER_TOKEN> and <METRICOOL_USER_ID> with your Metricool API and ID information:

```json
{
    "mcpServers": {
        "mcp-metricool": {
            "command": "uv",
            "args": [
                "--directory",
                "C:/Users/your-path/metricool-mcp",
                "run",
                "server.py"
            ],
            "env": {
                "METRICOOL_USER_TOKEN": "<METRICOOL_USER_TOKEN>",
                "METRICOOL_USER_ID": "<METRICOOL_USER_ID>"
            }
        }
    }
}
```

## Tools
The server implements several tools to interact with the Metricool API:

1. `get_brands(state: str)`
   - Get the list of brands from your Metricool account.

2. `get_Instagram_Reels(init_date: str, end_date: str, blog_id: int)`
   - Get the list of Instagram Reels from your Metricool account.

3. `get_Instagram_Posts(init_date: str, end_date: str, blog_id: int)`
   - Get the list of Instagram Posts from your Metricool account.

4. `get_Instagram_Stories(init_date: str, end_date: str, blog_id: int)`
   - Get the list of Instagram Stories from your Metricool account.

5. `get_Tiktok_Videos(init_date: str, end_date: str, blog_id: int)`
   - Get the list of Tiktok Videos from your Metricool account.

6. `get_Facebook_Reels(init_date: str, end_date: str, blog_id: int)`
   - Get the list of Facebook Reels from your Metricool account.

7. `get_Facebook_Posts(init_date: str, end_date: str, blog_id: int)`
   - Get the list of Facebook Posts from your Metricool brand account.

8. `get_Facebook_Stories(init_date: str, end_date: str, blog_id: int)`
   - Get the list of Facebook Stories from your Metricool brand account.

9. `get_Thread_Posts(init_date: str, end_date: str, blog_id: int)`
   - Get the list of Threads Posts from your Metricool brand account.

10. `get_X_Posts(init_date: str, end_date: str, blog_id: int)`
    - Get the list of X (Twitter) Posts from your Metricool account.

11. `get_Bluesky_Posts(init_date: str, end_date: str, blog_id: int)`
    - Get the list of Bluesky Posts from your Metricool brand account.

12. `get_Linkedin_Posts(init_date: str, end_date: str, blog_id: int)`
    - Get the list of Linkedin Posts from your Metricool brand account.

13. `get_Pinterest_Pins(init_date: str, end_date: str, blog_id: int)`
    - Get the list of Pinterest Pins from your Metricool brand account.

14. `get_Youtube_Videos(init_date: str, end_date: str, blog_id: int)`
    - Get the list of Youtube Videos from your Metricool brand account.

15. `get_Twitch_Videos(init_date: str, end_date: str, blog_id: int)`
    - Get the list of Twitch Videos from your Metricool account.

16. `get_FacebookAds_Campaigns(init_date: str, end_date: str, blog_id: int)`
    - Get the list of Facebook Ads Campaigns from your Metricool account.

17. `get_GoogleAds_Campaigns(init_date: str, end_date: str, blog_id: int)`
    - Get the list of Google Ads Campaigns from your Metricool account.

18. `get_TiktokAds_Campaigns(init_date: str, end_date: str, blog_id: int)`
    - Get the list of Tiktok Ads Campaigns from your Metricool brand account.