import httpx

from .errors import AuthenticationError, InvalidCredentials

class User:
    def __init__(self, *args, **kwargs) -> None:
        self.id = kwargs.get("id", None)
        self.admin = kwargs.get("admin", None)
        self.username = kwargs.get("username", None)
        self.email = kwargs.get("email", None)
        self.fist_name = kwargs.get("first_name", None)
        self.last_name = kwargs.get("last_name", None)
        self.language = kwargs.get("language", None)
        self.deleted = False
        
    def get_servers(self) -> list:
        pass
    
    def update(self, username, first_name, last_name, language, password, email) -> None:
        if not self.admin:
            raise AuthenticationError("You must be an admin to update a account")
        resp = self.client.post(f"{self.panel_url}/api/application/users/{self.id}", json={
            "email": email,
            "username": username,
            "first_name": first_name,
            "last_name": last_name,
            "language": language,
            "password": password
        })
        if resp.status_code == 200:
            self.__init__(**resp.json()["attributes"])
        else:
            raise Exception("Unknown error occured")
            
    def delete(self) -> None:
        if not self.admin:
            raise AuthenticationError("You must be an admin to delete a account")
        resp = self.client.delete(f"{self.panel_url}/api/application/users/{self.id}")
        if resp.status_code == 204:
            self.deleted = True
        else:
            raise Exception("Unknown error occured")
        
    def __str__(self) -> str:
        return f"<User id={self.id} username={self.username} email={self.email}>"