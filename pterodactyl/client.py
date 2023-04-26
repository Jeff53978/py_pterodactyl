import httpx

from .errors import AuthenticationError

class Client:
    def __init__(self, panel_url, api_key):
        self.panel_url = panel_url
        self.api_key = api_key
        self.client = httpx.Client()
        self.client.headers.update({
            "Authorization": f"Bearer {self.api_key}",
        })
        resp = self.client.get(f"{self.panel_url}/api/client/permissions")
        if resp.status_code == 400 or resp.status_code == 302:
            raise AuthenticationError("Improper API key passed")