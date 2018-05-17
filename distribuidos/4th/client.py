import socket
from threading import Thread, Lock
import time, sys

time_lock = Lock()

SEQ_ADDR = ('127.0.0.1', 5000)

class Client:
    def __init__(self, time, delta):
        self.delta = delta
        self.seq_ip, self.seq_port = SEQ_ADDR
        self.time = time
        
    def connect_to_sequencer(self):
        self.con_to_seq = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        while True:
            try:
                self.con_to_seq.connect((self.seq_ip, self.seq_port))
                break
            except socket.error:
                self.seq_port += 1
                print self.seq_port

    def update_time(self):
        while True:
            time_lock.acquire()
            self.time += self.delta
            time_lock.release()
            time.sleep(1)

    def wait_for_update(self):
        while True:
            daemon_time = int(self.con_to_seq.recv(256))
            time_lock.acquire()
            self.con_to_seq.send(str(self.time - daemon_time))
            time_lock.release()
            difference = int(self.con_to_seq.recv(256))
            time_lock.acquire()
            print self.time, 
            self.time += difference
            print self.time
            time_lock.release()


if __name__ == "__main__":
    cl = Client(int(sys.argv[1]), int(sys.argv[2]))
    cl.connect_to_sequencer()
    t = Thread(target=cl.update_time, args = ())
    t.daemon = True
    t.start()
    cl.wait_for_update()