import socket
import time
from threading import Thread, Lock

MAX_TIME = 3600

mutex = Lock()

latency = []
avgLatency = 0
quantity = 0

def getPing(file_name):
	global avgLatency
	global quantity
	f = open(file_name, 'w')
	for i in range(MAX_TIME):
		time.sleep(1)
		mutex.acquire()
		if quantity > 0:
			f.write("%.8f " % (avgLatency/quantity))
		else:
			f.write('0 ')
		avgLatency = quantity = 0
		mutex.release()
	f.close()

def beClient(HOST, PORT):
	global quantity
	global avgLatency
	tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	dest = (str(HOST), PORT)
	tcp.connect(dest)
	size = 128
	beginning = time.time()
	while time.time() - beginning < MAX_TIME:
		sent = time.time()
		tcp.send(str.encode(str(['']*size)))
		msg = tcp.recv(1024)
		quantity += 1
		ping = time.time() - sent
		avgLatency += ping
		print (ping)
	tcp.close()

pings = Thread(target = getPing, args = ("latencies", ))
pings.start()
t = Thread(target = beClient, args = ('192.168.0.23', 1100))
t.start()
