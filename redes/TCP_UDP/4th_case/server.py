import socket
import time
from threading import Thread, Lock
from operator import truediv
import os

MAX_TIME = 300
MAX_SERVERS = 32
flux = []
received = 0
clients = 0
def handle(con):
    global clients
    global received
    clients += 1
    while True:
        msg = con.recv(1024)
        msg = msg.decode("utf-8")
        con.send(str.encode('a'*len(msg))))
        if not msg:
            break
    con.close()
    clients -= 1

def serve(host, port):
    tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    orig = (HOST, PORT)
    tcp.bind(orig)
    tcp.listen(50)
    beginning = time.time()
    getf = Thread(target = getFlux, args = ("flux", ))
    getf.start()
    while time.time() - beginning < MAX_TIME:
        received = 0
        con, cliente = tcp.accept()
        print ("received connection:", cliente)
        ha = Thread(target = handle, args = (con, ))
        ha.start()
servers = []
for i in range(MAX_SERVERS):
    servers.append(Thread(target = serve, args = ('', 1100 + i)))
for server in servers:
    server.start()
