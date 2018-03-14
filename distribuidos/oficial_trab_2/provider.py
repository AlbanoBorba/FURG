#coding: utf-8
'''
Classe do Fornecedor
variáveis:
    - ws_name (string): nome do workspace;
    - server_host (string): IP do servidor;
    - server_port (string): porta do servidor;
    - time_sleep (int): tempo para fornecer um produto (em segundos) [default=5];
    - batch_size (int): tamanho do lote. [default=10].
'''

from nws.client import NetWorkSpace
from time import sleep
from math import ceil
from rmi_manager import RMIManager
import Pyro4
from config import Config

cfg = Config()

@Pyro4.expose
class Provider:
    def __init__(self,ws_name='Estoque', time_sleep=1,batch_size=10):
        self.time_sleep=time_sleep
        self.batch_size=batch_size
        #self.rmi=RMIManager()
        self.workspace=NetWorkSpace(ws_name,cfg.ts_machine_ip,
                                    cfg.ts_machine_port,persistent=True)

    #Método para gerar lotes de um produto
    # product_amount (int): quantidade requisitada do produto.
    def generateBatch(self,product_amount):
        n_batchs=int(ceil((product_amount*1.0)/self.batch_size))
        delivery=0
        for i in range(n_batchs):
            sleep(self.time_sleep)
            delivery+=self.batch_size
        return delivery


    #Método que fornece uma quantidade do produto no espaço de tuplas
    # product_name (string): nome do produto;
    # product_amount (int): quantidade requisitada do produto
    def supply(self,product_name,product_amount):
        print 'Processando requisição para ('+str(product_name)+','+str(product_amount)+')'
        sleep(self.time_sleep)
        delivery=self.generateBatch(product_amount)
        self.workspace.store(product_name,delivery)
        print 'Requisição entregue'


def main():

    rmi=RMIManager()
    rmi.beServer('Fornecedor',Provider)

if __name__=="__main__":
    main()
