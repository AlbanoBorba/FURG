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
    msg = "a" * int(size)
    begin = time.time()
    while time.time() - begin < MAX_TIME:
        sent = time.time()
        s.sendto(msg, (host, port))
        d = s.recvfrom(1400)
        latency += time.time() - sent
        qtd += 1
        reply = d[0]
        if not msg == reply:
            lost += 1
    avgLatency = latency/qtd
    print lost/qtd, avgLatency
    s.close()

client = Thread(target = beClient, args = ('192.168.0.23', 1100, sys.argv[1]))
client.start()
