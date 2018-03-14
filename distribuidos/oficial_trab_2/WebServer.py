import SOAPpy
from mq_manager import MQManager 
from Queue import Queue
from threading import Lock, Thread

from config import Config

cfg = Config()

mutex_teste = Lock()
prontos = []
num_pedido = 0
lpendentes = Queue()
lprontos = Queue()

def Pesquisar(num_pedido):
	if num_pedido in prontos:
		return 'Pedido Entregue!'
	else:
		return 'Pedido Pendente!'	
	
def Comprar(produto, quantidade):
	global num_pedido
	mutex_teste.acquire()
	num_pedido+=1	
	mutex_teste.release()
	i = 0
	for p, q in zip(produto, quantidade):
		if (i==0):
			saida = str(num_pedido)+':'+p+',0/'+str(q)+'|'
			i = 1
		else:
			saida = saida+p+',0/'+str(q)+'|'		
	saida = saida[:-1]
	lpendentes.put(saida)
	return num_pedido

def atualizarProntos():
	global prontos
	while True:	
		x = lprontos.get().split(":")[0]
		prontos.append(x)




def main():
	mq_prontos = MQManager(lprontos)
	t1 = Thread(target=mq_prontos.subscribeTo, args=('Prontos',))
	t1.daemon = True
	t1.start()
	mq_pendetes = MQManager(lpendentes)
	t2 = Thread(target=mq_pendetes.publishIn, args=('Pendentes',))
	t2.daemon = True
	t2.start()
	t3 = Thread(target=atualizarProntos, args=())
	t3.daemon = True
	t3.start()
	server = SOAPpy.SOAPServer((cfg.ws_machine_ip, 8080))
	server.registerFunction(Comprar, 'lojao','Comprar')
	server.registerFunction(Pesquisar, 'lojao','Pesquisar')
	server.serve_forever()


if __name__ == '__main__':
	main()