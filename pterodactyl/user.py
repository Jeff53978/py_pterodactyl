import httpx

from .errors import AuthenticationError, InvalidCredentials
from .server import Server

class User:
    def __init__(self, api, *args, **kwargs) -> None:
        if not kwargs.get("id", None):
            self.id = None
            self.admin = True
            self.username = None
            self.email = None
            self.fist_name = None
            self.last_name = None
            self.language = None
            self.deleted = False
            self.api = api
            return
        
        self.id = kwargs.get("id", None)
        self.admin = kwargs.get("admin", None)
        self.username = kwargs.get("username", None)
        self.email = kwargs.get("email", None)
        self.fist_name = kwargs.get("first_name", None)
        self.last_name = kwargs.get("last_name", None)
        self.language = kwargs.get("language", None)
        self.deleted = False
        self.api = api
        
    def get_servers(self) -> list:
        if not self.id:
            raise Exception("Application API does not have a user")
        try:
            servers = []
            resp = self.api.get(f"/api/application/servers?page=1&per_page=1000")
            for server in resp.json()["data"]:
                server = Server(**server["attributes"])
                if server.user == self.id:
                    servers.append(server)
        except:
            resp = self.api.get("/api/client")
            servers = []
            for server in resp.json()["data"]:
                server = Server(**server["attributes"])
                servers.append(server)
                
        return servers
    
    # Nog niet af
    def create_server(self, name, description, egg, docker_image, startup, limits, environment, feature_limits, allocation, location, **kwargs) -> Server:
        if not self.id:
            raise Exception("Application API does not have a user")
        if not self.admin:
            raise AuthenticationError("You must be an admin to create a server")
        resp = self.api.post("/api/application/servers", json={
            "name": name,
            "description": description,
            "egg": egg,
            "docker_image": docker_image,
            "startup": startup,
            "limits": limits,
            "environment": environment,
            "feature_limits": feature_limits,
            "allocation": allocation,
            "location": location,
            **kwargs
        })
        if resp.status_code == 422:
            raise Exception("Server already exists")
        return Server(**resp.json()["attributes"])
    
    def update(self, username, first_name, last_name, language, password, email) -> None:
        if not self.id:
            raise Exception("Application API does not have a user")
        if not self.admin:
            raise AuthenticationError("You must be an admin to update a account")
        resp = self.api.post(f"/api/application/users/{self.id}", json={
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
        if not self.id:
            raise Exception("Application API does not have a user")
        if not self.admin:
            raise AuthenticationError("You must be an admin to delete a account")
        resp = self.api.delete(f"/api/application/users/{self.id}")
        if resp.status_code == 204:
            self.deleted = True
        else:
            raise Exception("Unknown error occured")
        
    def __str__(self) -> str:
        return f"<User id={self.id} username={self.username} email={self.email}>"