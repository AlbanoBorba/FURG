import socket
import time
from threading import Thread, Lock
from operator import truediv
import os

MAX_TIME = 60

flux = []
received = 0
clients = 0
mutex_re = Lock()
mutex_cl = Lock()

def getFlux(file_name):
    global clients
    global received
    count = 0
    f = open(file_name, 'w')
    for i in range(MAX_TIME):
        time.sleep(1)
        mutex_re.acquire()
        f.write(str(received) + ' ')
        received = 0
        mutex_re.release()
    f.close()

def serve(host, port):
    received = 0
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind((HOST, PORT))
    while True:
        d = s.recvfrom(1024)
        data = d[0]
        addr = d[1]
        if not data:
            break
        received += 1
        s.sendto("ok" + data, addr)
    s.close()

serve('', 1100)
