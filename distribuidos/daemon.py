import socket
from threading import Thread, Lock
import time
import sys

time_lock = Lock()

SEQ_ADDR = ('127.0.0.1', 5000)

class Daemon:
    def __init__(self, time):
        self.ip, self.port = SEQ_ADDR
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.cons = []
        self.time = time

    def close_connection(self):
        self.sock.close()

    def update_time(self):
        while True:
            time_lock.acquire()
            self.time += 1
            time_lock.release()
            time.sleep(1)

    def handle(self):
        while True:
            time.sleep(3)
            media = 0
            atrasos = []
            for con in self.cons:
                con.send(str(self.time))
                tmp = int(con.recv(256))
                atrasos.append(tmp)
                media += tmp
            media /= len(self.cons)
            print atrasos, media,
            time_lock.acquire()
            self.time += media
            print self.time
            time_lock.release()
            for i in range(len(self.cons)):
                self.cons[i].send(str(media - atrasos[i]))

    def serve(self):
        while True:
            origin = (self.ip, self.port)
            try:
                self.sock.bind(origin)
                break
            except socket.error:
                self.port += 1
                print self.port
        self.sock.listen(50)
        while True:
            try:
                print "server online"
                con, client = self.sock.accept()
            except KeyboardInterrupt:
                print "server sera desligado assim que " \
                      "a ultima conexao for encerrada"
                break
            print "received connection:", client
            self.cons.append(con)


if __name__ == "__main__":
    receiver = Daemon(int(sys.argv[1]))
    t = Thread(target=receiver.update_time, args=())
    t1 = Thread(target=receiver.serve, args=())
    t.start()
    t1.start()
    raw_input()
    receiver.handle()
