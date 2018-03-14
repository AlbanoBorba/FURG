import socket
import time
from threading import Thread, Lock

MAX_TIME = 3600
def beClient(HOST, PORT):
	global quantity
	global avgLatency
	tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	dest = (str(HOST), PORT)
	tcp.connect(dest)
	size = 128
	beginning = time.time()
	while True:
		sent = time.time()
		if time.time() - beginning < MAX_TIME:
			tcp.send(str.encode(' '*size))
			msg = tcp.recv(1024)
		else:
			break
	tcp.close()

clients = []
for i in range(900):
	clients.append(Thread(target = beClient, args = ('192.168.0.23', 1100)))
for t in clients:
	t.start()
	time.sleep(10)
