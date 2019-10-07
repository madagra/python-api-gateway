from socket import inet_aton
from zeroconf import Zeroconf, ServiceInfo


class ZeroConfRegistration:

    def __init__(self, name, port):
        self.name = name
        self.port = port
        self.zeroconf = Zeroconf()

        desc: dict = {
            'docker_address': f"{name}:{port}",
        }
        self.info = ServiceInfo(
            "_http._tcp.local.",
            f"{self.name}._http._tcp.local.",
            addresses=[inet_aton("127.0.0.1")],
            port=self.port,
            properties=desc,
        )
        self.zeroconf.register_service(self.info)

    def unregister(self):
        self.zeroconf.unregister_service(self.info)
        self.zeroconf.close()
