class HealthCheck:
    _instance = None
    # _servers = []

    def __new__(cls):
        if not HealthCheck._instance:
            HealthCheck._instance = super(HealthCheck, cls).__new__(cls)
            cls._servers = []
        return HealthCheck._instance

    def addServer(self):
        self._servers.append("Server 1")
        self._servers.append("Server 2")

    def changeServer(self):
        self._servers.pop()
        self._servers.append("Server 5")

hc1 = HealthCheck()
hc1.addServer()
hc2 = HealthCheck()
hc2.addServer()
print(hc1._servers)
print(hc2._servers)