import httpx

class ResourceLimits:
    def __init__(self, *args, **kwargs):
        self.memory = kwargs.get("memory", None)
        self.swap = kwargs.get("swap", None)
        self.disk = kwargs.get("disk", None)
        self.io = kwargs.get("io", None)
        self.cpu = kwargs.get("cpu", None)
        self.threads = kwargs.get("threads", None)
        
    def __str__(self) -> str:
        return f"<ResourceLimits memory={self.memory} swap={self.swap} disk={self.disk} io={self.io} cpu={self.cpu} threads={self.threads}>"
        
class FeatureLimits:
    def __init__(self, *args, **kwargs):
        self.databases = kwargs.get("databases", None)
        self.allocations = kwargs.get("allocations", None)
        self.backups = kwargs.get("backups", None)
        
    def __str__(self) -> str:
        return f"<FeatureLimits databases={self.databases} allocations={self.allocations} backups={self.backups}>"
        
class ContainerOptions:
    def __init__(self, *args, **kwargs):
        self.startup_command = kwargs.get("startup_command", None)
        self.image = kwargs.get("image", None)
        self.installed = kwargs.get("installed", None)
        self.environment = kwargs.get("environment", {})
    
    def __str__(self) -> str:
        return f"<ContainerOptions startup_command={self.startup_command} image={self.image} installed={self.installed}>"

class Server:
    def __init__(self, *args, **kwargs):
        self.id = kwargs.get("id", None)
        self.external_id = kwargs.get("external_id", None)
        self.uuid = kwargs.get("uuid", None)
        self.identifier = kwargs.get("identifier", None)
        self.name = kwargs.get("name", None)
        self.description = kwargs.get("description", None)
        self.suspended = kwargs.get("suspended", None)
        self.limits = ResourceLimits(**kwargs.get("limits", {}))
        self.feature_limits = FeatureLimits(**kwargs.get("feature_limits", {}))
        self.user = kwargs.get("user", None)
        self.node = kwargs.get("node", None)
        self.allocation = kwargs.get("allocation", None)
        self.nest = kwargs.get("nest", None)
        self.egg = kwargs.get("egg", None)
        self.pack = kwargs.get("pack", None)
        self.container = ContainerOptions(**kwargs.get("container", {}))
        
    def __str__(self) -> str:
        return f"<Server id={self.id} external_id={self.external_id} uuid={self.uuid} identifier={self.identifier} name={self.name} description={self.description} suspended={self.suspended} limits={self.limits} feature_limits={self.feature_limits} user={self.user} node={self.node} allocation={self.allocation} nest={self.nest} egg={self.egg} pack={self.pack} container={self.container}>"
        