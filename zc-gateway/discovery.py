from time import sleep
from threading import Thread
from zeroconf import ServiceBrowser, Zeroconf, ZeroconfServiceTypes, ServiceStateChange


class InvalidServiceAddedException(Exception):
    pass


class InvalidServiceRemovedException(Exception):
    pass


class ZeroConfDiscovery(Thread):

    def __init__(self):
        super().__init__()
        self.services = {}
        self.zeroconf = Zeroconf()

    def on_service_change(self, zeroconf, service_type, name, state_change):
        print("Service %s of type %s state changed: %s" % (name, service_type, state_change))
        try:
            service_name = name.split(".")[0]
            if state_change is ServiceStateChange.Added:
                info = self.zeroconf.get_service_info(service_type, name)
                service_port = info.port
                self.services[service_name] = f"{service_name}:{service_port}"
            elif state_change is ServiceStateChange.Removed:
                found = self.services.pop(service_name, None)
                if found is None:
                    raise InvalidServiceRemovedException(f"The service removed is not valid.")

        except (Exception, KeyError) as e:
            raise InvalidServiceAddedException(f"The name or properties of the service "
                                               f"added are not valid: {e}")

    def run(self):
        _ = ServiceBrowser(self.zeroconf, "_http._tcp.local.", handlers=[self.on_service_change])
        try:
            while True:
                ZeroconfServiceTypes.find()
                sleep(10)
        except (KeyboardInterrupt, InvalidServiceAddedException):
            pass
        finally:
            self.zeroconf.close()
