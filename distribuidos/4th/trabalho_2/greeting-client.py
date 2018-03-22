from rmi_manager import RMIManager


rmi = RMIManager()
cl = rmi.requireClass('Fornecedor', "192.168.1.102", 9090)
cl.k("tetola")
