import socket
import sys
def serve(host, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind((host, port))
    while True:
        d = s.recvfrom(1400)
        data = d[0]
        addr = d[1]
        if not data:
            break
        s.sendto(data, addr)
    s.close()

serve('', 1100)
