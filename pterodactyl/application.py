import httpx

from .errors import AuthenticationError

class ApplicationClient:
    def __init__(self, panel_url, api_key):
        self.panel_url = panel_url
        self.api_key = api_key
        self.client = httpx.Client()