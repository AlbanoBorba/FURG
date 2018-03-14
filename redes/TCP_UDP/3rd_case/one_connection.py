import socket
import time
import sys
from threading import Thread, Lock

MAX_TIME = 120
quantity = 0
avgLatency = 0

def beClient(HOST, PORT, size):
	global quantity
	global avgLatency
	tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	dest = (str(HOST), PORT)
	tcp.connect(dest)
	beginning = time.time()
	while True:
		sent = time.time()
		if time.time() - beginning < MAX_TIME:
			tcp.sendall(str.encode(' '*int(size)))
			msg = tcp.recv(1024)
			quantity += 1
		else:
			break
		ping = time.time() - sent
		avgLatency += ping
		print (ping)
	print "final", avgLatency/quantity
	tcp.close()

client = Thread(target = beClient, args = ('192.168.0.23', 1100, sys.argv[1]))
client.start()
