import socket
import time
from threading import Thread, Lock

MAX_TIME = 120

mutex = Lock()

latency = []
avgLatency = 0
quantity = 0

def getPing(file_name):
	global avgLatency
	global quantity
	f = open(file_name, 'w')
	f.write("latency = [")
	for i in range(MAX_TIME - 1):
		time.sleep(1)
		mutex.acquire()
		if quantity > 0:
			f.write(str(avgLatency/quantity) + ', ')
		else:
			f.write('0, ')
		avgLatency = quantity = 0
		mutex.release()
	time.sleep(1)
	if quantity > 0:
		f.write(str(avgLatency/quantity) + ']')
	else:
		f.write('0]')
	f.close()

def beClient(HOST, PORT):
	global quantity
	global avgLatency
	HOST = ''
	PORT = 1100
	dest = (str(HOST), PORT)
	size = 32
	beginning = time.time()
	for msgs in range(10000):
		tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		tcp.connect(dest)
		tcp.send(str.encode(str(['']*size)))
		msg = tcp.recv(1024)
		tcp.close()
	print time.time() - beginning

clients = []
pings = Thread(target = getPing, args = ("latencies", ))
pings.start()
for i in range(20):
	clients.append(Thread(target = beClient, args = ('172.16.1.169', 1100)))
for t in clients:
	t.start()
