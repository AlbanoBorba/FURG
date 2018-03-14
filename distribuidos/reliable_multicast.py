import socket
from threading import Thread, Lock
import sys, os

ips = ['127.0.0.1:1200', '127.0.0.1:1201', '127.0.0.1:1202']

print_lock = Lock()

class Member:
    def __init__(self, ind):
        self.id = ind
        self.ip, self.port = ips[ind].split(":")
        self.port = int(self.port)
        self.received = []
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.cons = []
        
    def connect_to_others(self):
        for i in range(len(ips)):
            ip, port = ips[i].split(":")
            if i != self.id:
                tmp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                #print ip, port
                tmp.connect((ip, int(port)))
                #print "connected to", ip, port
                self.cons.append(tmp)

    def multicast(self, message, identifier=None):
        if identifier == None:
            identifier = self.id
        #print message, identifier
        for con in self.cons:
            con.send(str(identifier) + ";" + str(message))

    def handle(self, con):
        while True:
            try:
                msg = con.recv(256)
            except socket.error as e:
                print e
                break
            identifier, message = msg.split(";")
            #print message, self.received, message in self.received
            if message not in self.received:
                self.received.append(message)
                if self.id != identifier:
                    self.multicast(message, identifier)
                print_lock.acquire()
                print message
                print_lock.release()

    def serve(self):
        while True:
            origin = (self.ip, self.port)
            try:
                self.sock.bind(origin)
                break
            except socket.error:
                self.port += 1
                #print self.port
        self.sock.listen(50)
        while True:
            try:
                #print "server online"
                con, client = self.sock.accept()
            except KeyboardInterrupt:
                break
            #print "received connection:", client
            self.cons.append(con)
            h = Thread(target=self.handle, args=(con, ))
            h.daemon = True
            h.start()


if __name__ == "__main__":
    #print sys.argv
    mem = Member(int(sys.argv[1]))
    t = Thread(target=mem.serve, args=())
    t.daemon = True
    t.start()
    print mem.ip, mem.port
    raw_input()
    mem.connect_to_others()

    while True:
        message = raw_input()
        mem.multicast(message)