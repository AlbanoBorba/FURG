import socket
import time
from threading import Thread, Lock

MAX_TIME = 200
def beClient(HOST, PORT):
	global quantity
	global avgLatency
	tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	dest = (str(HOST), PORT)
	tcp.connect(dest)
	size = 32
	beginning = time.time()
	while True:
		sent = time.time()
		if time.time() - beginning < MAX_TIME:
			tcp.send(str.encode(str(['']*size)))
			msg = tcp.recv(1024)
		else:
			break
	tcp.close()

clients = []
for i in range(20):
	clients.append(Thread(target = beClient, args = ('172.16.1.169', 1100)))
for t in clients:
	t.start()
