import time
import requests

MAX_ATTEMPTS = 3


def fetch_weather(url: str, params: dict) -> dict:
    """Fetch current weather, retrying on transient failure."""
    # Loop over attempt numbers from 1 to MAX_ATTEMPTS inclusive. Each attempt: issue a GET request with params and a 10-second timeout, raise on a bad HTTP status, and return the JSON body on success. On the final attempt, let the exception propagate instead of retrying.
    response = requests.get(url, params=params, timeout=10)
    response.raise_for_status()
    return response.json()


def parse_response(raw: dict) -> dict:
    """Extract the fields the pipeline actually needs, defensively."""
    current = raw.get("current", {})
    return {
        "temp": current.get("temp"),
        "humidity": current.get("humidity"),
        "wind_speed": current.get("wind_speed"),
    }
