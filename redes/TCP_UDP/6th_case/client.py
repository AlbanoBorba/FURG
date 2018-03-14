import socket
import time
from threading import Thread, Lock

def beClient(HOST, PORT):
	tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	dest = (str(HOST), PORT)
	tcp.connect(dest)
	tcp.send(str.encode("se liga parceiro"))
	time.sleep(30)
	tcp.close()

client = (Thread(target = beClient, args = ('192.168.0.23', 1100)))
client.start()
