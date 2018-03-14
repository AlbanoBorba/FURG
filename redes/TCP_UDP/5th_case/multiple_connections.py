import socket
import time
from threading import Thread, Lock

results = []

def beClient(HOST, PORT, size):
	beginning = time.time()
	dest = (str(HOST), PORT + i)
	tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	tcp.connect(dest)
	tcp.send(str.encode(str(['']*size)))
	msg = tcp.recv(1024)
	tcp.close()
	results.append(time.time() - beginning)

client = Thread(target = beClient, args = ('172.16.1.169', 1100, 32)))
client.start()
