import socket
import time
from threading import Thread, Lock

MAIN_TIME = 240
AUX_TIME = 60
MAX_CLIENTS = 240

mutex = Lock()

avgLatency = 0
quantity = 0

def getPing(file_name):
	global avgLatency
	global quantity
	f = open(file_name, 'w')
	for i in range(MAIN_TIME):
		time.sleep(1)
		mutex.acquire()
		if quantity > 0:
			f.write("%.8f " % (avgLatency/quantity))
		else:
			f.write('0 ')
		avgLatency = 0
		quantity = 0
		mutex.release()
	f.close()

def mainClient(host, port, size):
	global avgLatency
	global quantity
	lost = 0
	count = 0
	s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	msg = "a" * size
	begin = time.time()
	while time.time() - begin < MAIN_TIME:
		sent = time.time()
		s.sendto(msg, (host, port))
		d = s.recvfrom(1024)
		latency = time.time() - sent
		avgLatency += latency
		quantity += 1
		count += 1
		print latency
		reply = d[0]
		if not msg == reply:
			lost += 1
	print lost/count
	s.close()

def auxClient(host, port, size):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    msg = "a" * size
    begin = time.time()
    while begin - time.time() < AUX_TIME:
        s.sendto(msg, (host, port))
        d = s.recvfrom(1024)
    s.close()

p = Thread(target = getPing, args = ("latencies", ))
p.start()

main = Thread(target = mainClient, args = ('192.168.0.23', 1100, 128))
main.start()


auxiliars = []
for i in range(MAX_CLIENTS):
    auxiliars.append(Thread(target = auxClient, args = ('192.168.0.23', 1100, 128)))
for aux in auxiliars:
    aux.start()
    time.sleep(1)
