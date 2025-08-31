import requests
from info import SHORTENER_API, SHORTENER_WEBSITE


def shorten_url(url: str) -> str:
    """
    Shortens the given URL using your shortener service (earnlinks.in).
    Falls back to original URL if API fails.
    """
    try:
        api = SHORTENER_API
        domain = SHORTENER_WEBSITE
        short_url = f"https://{domain}/api?api={api}&url={url}"

        response = requests.get(short_url).json()
        if response.get("status") == "success":
            return response["shortenedUrl"]
        else:
            return url
    except Exception as e:
        print(f"Shortener error: {e}")
        return url
