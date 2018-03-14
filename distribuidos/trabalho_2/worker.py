from mq_manager import MQManager
from rmi_manager import RMIManager
from ts_manager import TSManager
from utils import organizeOrder, isReady, askForSupply, deorganizeOrder

from Queue import Queue, Empty
from threading import Thread
from config import Config

cfg = Config()

class Worker:

    def __init__(self, ready_name, waiting_name):
        self.ready = Queue()
        self.waiting = Queue()
        self.ready_mq = MQManager(self.ready)
        self.waiting_mq = MQManager(self.waiting)
        self.startMQ(ready_name, waiting_name)
        self.rmi = RMIManager()
        self.ts = TSManager()
        self.provider = self.rmi.requireClass('Fornecedor',
                                              cfg.rmi_machine_ip,
                                              cfg.rmi_machine_port)
        #

    def startMQ(self, ready_name, waiting_name):
        threads = []
        threads.append(Thread(target=self.ready_mq.publishIn,
                              args=(ready_name,)))
        threads.append(Thread(target=self.waiting_mq.subscribeTo,
                              args=(waiting_name,)))

        for thread in threads:
            thread.daemon = True
            thread.start()

    def checkWaiting(self):
        while True:
            to_go = []
            while True:
                try:
                    waiting_order = self.waiting.get_nowait()
                    print waiting_order
                except Empty:
                    break
                content = organizeOrder(waiting_order)
                new_order = self.ts.checkStock(content)
                if isReady(new_order):
                    as_str = deorganizeOrder(new_order)
                    print as_str
                    self.ready.put(as_str)
                else:
                    askForSupply(new_order, self.provider)
                    to_go.append(new_order)
            for item in to_go:
                item_str = deorganizeOrder(item)
                self.waiting.put(item_str)




def main():
    wrk = Worker('Prontos', 'Pendentes')
    wrk.checkWaiting()

if __name__ == "__main__":
    main()
