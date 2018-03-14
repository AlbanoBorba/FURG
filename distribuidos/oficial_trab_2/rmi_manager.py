import Pyro4
from config import Config

cfg = Config()

class RMIManager:

    def beServer(self, name, cl):
        daemon = Pyro4.Daemon(host=cfg.this_machine)
        ns = Pyro4.locateNS()
        uri = daemon.register(cl)
        print uri
        ns.register(name, uri)

        print ("Ready.")
        daemon.requestLoop()

    def requireClass(self, name, ip, port):
        ns = Pyro4.locateNS(ip, port)
        uri = ns.lookup(name)
        return Pyro4.Proxy(uri)
