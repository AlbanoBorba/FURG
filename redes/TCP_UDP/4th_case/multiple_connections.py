import socket
import time
from threading import Thread, Lock
import matplotlib.pyplot as plt

results = []

def beClient(HOST, PORT, size):
	for quantity in range(64):
		beginning = time.time()
		for i in range(quantity):
			dest = (str(HOST), PORT + i)
			tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			tcp.connect(dest)
			tcp.send(str.encode(str(['']*size)))
			msg = tcp.recv(1024)
			tcp.close()
		results.append(time.time() - beginning)
	plt.plot(results)
	plt.show()
client = Thread(target = beClient, args = ('192.168.0.23', 1100, 32))
client.start()
