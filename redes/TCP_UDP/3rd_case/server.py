import socket
import time
from threading import Thread, Lock
from operator import truediv
import os

MAX_TIME = 300

flux = []
received = 0
clients = 0
mutex_re = Lock()

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

def handle(con):
    global clients
    global received
    clients += 1
    while True:
        msg = con.recv(4096)
        msg = msg.decode("utf-8")
        con.send(str.encode(str(['']*len(msg))))
        if msg:
            mutex_re.acquire()
            received += 1
            mutex_re.release()
        else:
            break
    con.close()
    clients -= 1


HOST = ''
PORT = 1100
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
