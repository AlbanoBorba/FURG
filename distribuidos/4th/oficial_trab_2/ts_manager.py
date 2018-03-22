from nws.client import NetWorkSpace
from config import Config
cfg = Config()

class TSManager:

    def __init__(self):
        self.ws = NetWorkSpace('Estoque', cfg.ts_machine_ip, cfg.ts_machine_port, persistent=True)

    def put(self, item_name, quantity):
        self.ws.store(item_name, quantity)

    def get(self, item_name):
        available = self.ws.fetchTry(item_name)
        return available

    def checkStock(self, content):
        new_order = content
        for item in new_order["items"]:
            left =  item["need"] - item["have"]
            while item["need"] > item["have"]:
                in_stock = self.get(item["name"])
                if in_stock == None:
                    break
                got = min(in_stock, left)
                item["have"] += got
                in_stock -= got
                if in_stock > 0:
                    self.put(item["name"], in_stock)

        return new_order
