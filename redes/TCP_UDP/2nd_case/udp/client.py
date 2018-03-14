import socket
import sys
import time
from threading import Thread, Lock

MAX_TIME = 30

def beClient(host, port, size):
    latency = 0
    qtd = 0
    lost = 0
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    msg = " " * size
    begin = time.time()
    for i in range(10000):
        s.sendto(msg, (host, port))
        d = s.recvfrom(1024)
        reply = d[0]
        if not msg == reply:
            lost += 1
    print time.time() - begin
    print "%d msgs lost" % lost
    s.close()

client = []
for i in range(20):
    client.append(Thread(target = beClient, args = ('', 1100, 32)))
for c in client:
    c.start()
