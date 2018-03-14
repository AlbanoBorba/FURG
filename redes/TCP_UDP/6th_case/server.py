import socket
import time
import os
from threading import Thread, Lock

def serve(host, port):
    tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    orig = (host, port)
    tcp.bind(orig)
    tcp.listen(50)
    con, cliente = tcp.accept()
    print ("received connection:", cliente)
    msg = con.recv(1024)
    msg = msg.decode("utf-8")
    print msg
    msg = con.recv(1024)
    msg = msg.decode("utf-8")
    print msg
    con.close()

servers = []
for i in range(MAX_SERVERS):
    servers.append(Thread(target = serve, args = ('', 1100 + i)))
