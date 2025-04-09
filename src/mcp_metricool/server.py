from typing import Any
import httpx
from mcp.server.fastmcp import FastMCP
import os
from typing import List, Dict, Any


# Initialize FastMCP server
mcp = FastMCP("metricool")

# Constants
METRICOOL_BASE_URL = "https://app.metricool.com/api"
METRICOOL_USER_TOKEN = os.getenv("METRICOOL_USER_TOKEN")
METRICOOL_USER_ID = os.getenv("METRICOOL_USER_ID")


async def make_get_request(url: str) -> dict[str, Any] | None:
    """Make a get request to the Metricool API with proper error handling."""
    headers = {
        "X-Mc-Auth": METRICOOL_USER_TOKEN,
    }
    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(url, headers=headers, timeout=30.0)
            response.raise_for_status()
            return response.json()
        except Exception:
            return None
        
async def make_post_request(url: str, data: dict[str, Any]) -> dict[str, Any] | None:
    """Make a post request to the Metricool API with proper error handling."""
    headers = {
        "X-Mc-Auth": METRICOOL_USER_TOKEN,
    }
    async with httpx.AsyncClient() as client:
        try:
            response = await client.post(url, headers=headers, json=data, timeout=30.0)
            response.raise_for_status()
            return response.json()
        except Exception:
            return None

@mcp.tool()
async def get_brands(state: str) -> List[str]:
    """
    Get the list of brands from your Metricool account.
    """

    url = f"{METRICOOL_BASE_URL}/admin/simpleProfiles?userId={METRICOOL_USER_ID}"
    
    response = await make_get_request(url)

    if not response:
       return ("Failed to get brands")
    
    return response

@mcp.tool()
async def get_Instagram_Reels(init_date: str, end_date: str, blog_id: int) -> List[str]:
    """
    Get the list of Instagram Reels from your Metricool account.
    
    Args:
     init date: Init date of the period to get the data. The format is 2025-01-01
     end date: End date of the period to get the data. The format is 2025-01-01
     blog id: Blog id of the Metricool brand account.
    """

    url = f"{METRICOOL_BASE_URL}/v2/analytics/reels/instagram?from={init_date}T00%3A00%3A00&to={end_date}T00%3A00%3A00&blogId={blog_id}&userId={METRICOOL_USER_ID}"
    
    response = await make_get_request(url)

    if not response:
       return ("Failed to get Instagram Reels")
    
    return response

@mcp.tool()
async def get_Instagram_Posts(init_date: str, end_date: str, blog_id: int) -> List[str]:
    """
    Get the list of Instagram Posts from your Metricool account.
    
    Args:
     init date: Init date of the period to get the data. The format is 2025-01-01
     end date: End date of the period to get the data. The format is 2025-01-01
     blog id: Blog id of the Metricool brand account.
    """

    url = f"{METRICOOL_BASE_URL}/v2/analytics/posts/instagram?from={init_date}T00%3A00%3A00&to={end_date}T00%3A00%3A00&blogId={blog_id}&userId={METRICOOL_USER_ID}"
    
    response = await make_get_request(url)

    if not response:
       return ("Failed to get Instagram Posts")
    
    return response

@mcp.tool()
async def get_Instagram_Stories(init_date: str, end_date: str, blog_id: int) -> List[str]:
    """
    Get the list of Instagram Stories from your Metricool account.
    
    Args:
     init date: Init date of the period to get the data. The format is 20250101
     end date: End date of the period to get the data. The format is 20250101
     blog id: Blog id of the Metricool brand account.
    """

    url = f"{METRICOOL_BASE_URL}/stats/instagram/stories?start={init_date}&end={end_date}&blogId={blog_id}&userId={METRICOOL_USER_ID}"
    
    response = await make_get_request(url)

    if not response:
       return ("Failed to get Instagram Stories")
    
    return response

@mcp.tool()
async def get_Tiktok_Videos(init_date: str, end_date: str, blog_id: int) -> List[str]:
    """
    Get the list of Tiktok Videos from your Metricool account.
    
    Args:
     init date: Init date of the period to get the data. The format is 2025-01-01
     end date: End date of the period to get the data. The format is 2025-01-01
     blog id: Blog id of the Metricool brand account.
    """

    url = f"{METRICOOL_BASE_URL}/v2/analytics/posts/tiktok?from={init_date}T00%3A00%3A00&to={end_date}T00%3A00%3A00&blogId={blog_id}&userId={METRICOOL_USER_ID}"
    
    response = await make_get_request(url)

    if not response:
       return ("Failed to get Tiktok Videos")
    
    return response

@mcp.tool()
async def get_Facebook_Reels(init_date: str, end_date: str, blog_id: int) -> List[str]:
    """
    Get the list of Facebook Reels from your Metricool account.
    
    Args:
     init date: Init date of the period to get the data. The format is 2025-01-01
     end date: End date of the period to get the data. The format is 2025-01-01
     blog id: Blog id of the Metricool brand account.
    """

    url = f"{METRICOOL_BASE_URL}/v2/analytics/reels/facebook?from={init_date}T00%3A00%3A00&to={end_date}T23%3A59%3A59&blogId={blog_id}&userId={METRICOOL_USER_ID}"
    
    response = await make_get_request(url)

    if not response:
       return ("Failed to get Facebook Reels")
    
    return response

@mcp.tool()
async def get_Facebook_Posts(init_date: str, end_date: str, blog_id: int) -> List[str]:
    """
    Get the list of Facebook Posts from your Metricool brand account.
    
    Args:
     init date: Init date of the period to get the data. The format is 2025-01-01
     end date: End date of the period to get the data. The format is 2025-01-01
     blog id: Blog id of the Metricool brand account.
    """

    url = f"{METRICOOL_BASE_URL}/v2/analytics/posts/facebook?from={init_date}T00%3A00%3A00&to={end_date}T23%3A59%3A59&blogId={blog_id}&userId={METRICOOL_USER_ID}"
    
    response = await make_get_request(url)

    if not response:
       return ("Failed to get Facebook Posts")
    
    return response

@mcp.tool()
async def get_Facebook_Stories(init_date: str, end_date: str, blog_id: int) -> List[str]:
    """
    Get the list of Facebook Stories from your Metricool brand account.
    
    Args:
     init date: Init date of the period to get the data. The format is 2025-01-01
     end date: End date of the period to get the data. The format is 2025-01-01
     blog id: Blog id of the Metricool brand account.
    """

    url = f"{METRICOOL_BASE_URL}/v2/analytics/stories/facebook?from={init_date}T00%3A00%3A00&to={end_date}T23%3A59%3A59&blogId={blog_id}&userId={METRICOOL_USER_ID}"
    
    response = await make_get_request(url)

    if not response:
       return ("Failed to get Facebook Stories")
    
    return response

@mcp.tool()
async def get_Thread_Posts(init_date: str, end_date: str, blog_id: int) -> List[str]:
    """
    Get the list of Threads Posts from your Metricool brand account.
    
    Args:
     init date: Init date of the period to get the data. The format is 2025-01-01
     end date: End date of the period to get the data. The format is 2025-01-01
     blog id: Blog id of the Metricool brand account.
    """

    url = f"{METRICOOL_BASE_URL}/v2/analytics/posts/threads?from={init_date}T00%3A00%3A00&to={end_date}T23%3A59%3A59&blogId={blog_id}&userId={METRICOOL_USER_ID}"
    
    response = await make_get_request(url)

    if not response:
       return ("Failed to get Threads Posts")
    
    return response

@mcp.tool()
async def get_X_Posts(init_date: str, end_date: str, blog_id: int) -> List[str]:
    """
    Get the list of X (Twitter) Posts from your Metricool account.
    
    Args:
     init date: Init date of the period to get the data. The format is 20250101
     end date: End date of the period to get the data. The format is 20250101
     blog id: Blog id of the Metricool brand account.
    """

    url = f"{METRICOOL_BASE_URL}/stats/twitter/posts?start={init_date}&end={end_date}&blogId={blog_id}&userId={METRICOOL_USER_ID}"
    
    response = await make_get_request(url)

    if not response:
       return ("Failed to get X Posts")
    
    return response

@mcp.tool()
async def get_Bluesky_Posts(init_date: str, end_date: str, blog_id: int) -> List[str]:
    """
    Get the list of Bluesky Posts from your Metricool brand account.
    
    Args:
     init date: Init date of the period to get the data. The format is 2025-01-01
     end date: End date of the period to get the data. The format is 2025-01-01
     blog id: Blog id of the Metricool brand account.
    """

    url = f"{METRICOOL_BASE_URL}/v2/analytics/posts/bluesky?from={init_date}T00%3A00%3A00&to={end_date}T23%3A59%3A59&blogId={blog_id}&userId={METRICOOL_USER_ID}"
    
    response = await make_get_request(url)

    if not response:
       return ("Failed to get Bluesky Posts")
    
    return response

@mcp.tool()
async def get_Linkedin_Posts(init_date: str, end_date: str, blog_id: int) -> List[str]:
    """
    Get the list of Linkedin Posts from your Metricool brand account.
    
    Args:
     init date: Init date of the period to get the data. The format is 2025-01-01
     end date: End date of the period to get the data. The format is 2025-01-01
     blog id: Blog id of the Metricool brand account.
    """

    url = f"{METRICOOL_BASE_URL}/v2/analytics/posts/linkedin?from={init_date}T00%3A00%3A00&to={end_date}T23%3A59%3A59&blogId={blog_id}&userId={METRICOOL_USER_ID}"
    
    response = await make_get_request(url)

    if not response:
       return ("Failed to get Linkedin Posts")
    
    return response

@mcp.tool()
async def get_Pinterest_Pins(init_date: str, end_date: str, blog_id: int) -> List[str]:
    """
    Get the list of Pinterest Pins from your Metricool brand account.
    
    Args:
     init date: Init date of the period to get the data. The format is 2025-01-01
     end date: End date of the period to get the data. The format is 2025-01-01
     blog id: Blog id of the Metricool brand account.
    """

    url = f"{METRICOOL_BASE_URL}/v2/analytics/posts/pinterest?from={init_date}T00%3A00%3A00&to={end_date}T23%3A59%3A59&blogId={blog_id}&userId={METRICOOL_USER_ID}"
    
    response = await make_get_request(url)

    if not response:
       return ("Failed to get Pinterest Pins")
    
    return response

@mcp.tool()
async def get_Youtube_Videos(init_date: str, end_date: str, blog_id: int) -> List[str]:
    """
    Get the list of Youtube Videos from your Metricool brand account.
    
    Args:
     init date: Init date of the period to get the data. The format is 2025-01-01
     end date: End date of the period to get the data. The format is 2025-01-01
     blog id: Blog id of the Metricool brand account.
    """

    url = f"{METRICOOL_BASE_URL}/v2/analytics/posts/youtube?from={init_date}T00%3A00%3A00&to={end_date}T23%3A59%3A59&blogId={blog_id}&userId={METRICOOL_USER_ID}"
    
    response = await make_get_request(url)

    if not response:
       return ("Failed to get Youtube Videos")
    
    return response

@mcp.tool()
async def get_Twitch_Videos(init_date: str, end_date: str, blog_id: int) -> List[str]:
    """
    Get the list of Twitch Videos from your Metricool account.
    
    Args:
     init date: Init date of the period to get the data. The format is 20250101
     end date: End date of the period to get the data. The format is 20250101
     blog id: Blog id of the Metricool brand account.
    """

    url = f"{METRICOOL_BASE_URL}/stats/twitch/videos?start={init_date}&end={end_date}&blogId={blog_id}&userId={METRICOOL_USER_ID}"
    
    response = await make_get_request(url)

    if not response:
       return ("Failed to get Twitch Videos")
    
    return response

@mcp.tool()
async def get_FacebookAds_Campaigns(init_date: str, end_date: str, blog_id: int) -> List[str]:
    """
    Get the list of Facebook Ads Campaigns from your Metricool account.
    
    Args:
     init date: Init date of the period to get the data. The format is 20250101
     end date: End date of the period to get the data. The format is 20250101
     blog id: Blog id of the Metricool brand account.
    """

    url = f"{METRICOOL_BASE_URL}/stats/facebookads/campaigns?start={init_date}&end={end_date}&blogId={blog_id}&userId={METRICOOL_USER_ID}"
    
    response = await make_get_request(url)

    if not response:
       return ("Failed to get Facebook Ads Campaigns")
    
    return response

@mcp.tool()
async def get_GoogleAds_Campaigns(init_date: str, end_date: str, blog_id: int) -> List[str]:
    """
    Get the list of Google Ads Campaigns from your Metricool account.
    
    Args:
     init date: Init date of the period to get the data. The format is 20250101
     end date: End date of the period to get the data. The format is 20250101
     blog id: Blog id of the Metricool brand account.
    """

    url = f"{METRICOOL_BASE_URL}/stats/adwords/campaigns?start={init_date}&end={end_date}&blogId={blog_id}&userId={METRICOOL_USER_ID}"
    
    response = await make_get_request(url)

    if not response:
       return ("Failed to get Google Ads Campaigns")
    
    return response

@mcp.tool()
async def get_TiktokAds_Campaigns(init_date: str, end_date: str, blog_id: int) -> List[str]:
    """
    Get the list of Tiktok Ads Campaigns from your Metricool brand account.
    
    Args:
     init date: Init date of the period to get the data. The format is 2025-01-01
     end date: End date of the period to get the data. The format is 2025-01-01
     blog id: Blog id of the Metricool brand account.
    """

    url = f"{METRICOOL_BASE_URL}/v2/analytics/campaigns/tiktokads?from={init_date}T00%3A00%3A00&to={end_date}T23%3A59%3A59&blogId={blog_id}&userId={METRICOOL_USER_ID}"
    
    response = await make_get_request(url)

    if not response:
       return ("Failed to get Tiktok Ads Campaigns")
    
    return response



if __name__ == "__main__":
    # Initialize and run the server
    mcp.run(transport='stdio')
