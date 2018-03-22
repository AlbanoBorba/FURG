from rmi_manager import RMIManager
import Pyro4

@Pyro4.expose
class Noia:
    def k(self):
        print "oi"

rmi = RMIManager()
rmi.beServer('Fornecedor', Noia)
