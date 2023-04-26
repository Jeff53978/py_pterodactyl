import httpx

from .errors import AuthenticationError, InvalidCredentials
from .user import User

class Client:
    def __init__(self, panel_url, api_key):
        self.api = HTTPClient(panel_url, api_key)
        resp = self.api.get(f"/api/client/account")
        if resp.status_code == 400 or resp.status_code == 302:
            raise InvalidCredentials("Improper API key passed")
        self.user = User(self.api, **resp.json()["attributes"])
        
class HTTPClient:
    def __init__(self, panel_url, api_key):
        self.panel_url = panel_url
        self.api_key = api_key
        self.client = httpx.Client()
        self.client.headers.update({
            "Authorization": f"Bearer {self.api_key}",
        })
        
    def get(self, url):
        return self.client.get(f"{self.panel_url}{url}")
    
    def post(self, url, json):
        return self.client.post(f"{self.panel_url}{url}", json=json)
    
    def delete(self, url):
        return self.client.delete(f"{self.panel_url}{url}")