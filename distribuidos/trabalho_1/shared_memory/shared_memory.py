#!/usr/bin/env python
# -*- coding: utf-8 -*-

import socket
from threading import Thread
from managers import SemaphoreManager, MemoryManager

class Server:

    def __init__(self, port, partition_size, m_key, s_key):
        self.ip = ''
        self.port = port
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.partition = MemoryManager(m_key, partition_size)
        self.sem = SemaphoreManager(s_key)

    def close_connection(self):
        self.sock.close()

    def handle(self, con):
        cmd = ""
        tmp = []
        while True:
            msg = con.recv(256)
            if msg == "quit":
                break
            try:
                cmd, pos, size, buff = msg.split('#', 3)
                print "done"
            except ValueError:
                print "connection cloooOOOsed"
                break
            pos = int(pos)
            size = int(size)
            print msg
            if cmd == "read":
                self.sem.acquire()
                value = self.partition.read(pos, size)
                self.sem.release()
                con.send(value)

            elif cmd == "write":
                self.sem.acquire()
                value = self.partition.write(pos, buff)
                self.sem.release()
                con.send(value)

    def serve(self):
        origin = (self.ip, self.port)
        print origin
        self.sock.bind(origin)
        self.sock.listen(50)
        while True:
            try:
                print "server online"
                con, client = self.sock.accept()
            except KeyboardInterrupt:
                print "server será desligado assim que " \
                      "a última conexão for encerrada"
                self.partition.delete()
                self.sem.delete()
                break
            print "received connection:", client
            h = Thread(target=self.handle, args=(con, ))
            h.start()


class Client:

    def __init__(self, hosts_path):
        f = open(hosts_path, "r")
        lines = f.readlines()
        self.host_list = lines[0].split(";")
        self.cons = []
        self.partition_size = int(lines[1].split("=")[1])
        self.memory_size = self.partition_size * len(self.host_list)

    def establish_connections(self):
        hosts = []
        for i, host in enumerate(self.host_list):
            addr, port = host.split(":")
            print 'connecting to', addr, port
            tmp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            tmp.connect((addr, int(port)))
            self.cons.append(tmp)

    def send_msg(self, msgs, cons):
        result = ""
        for con, msg in zip(cons, msgs):
            print msg, con
            con.sendall(msg)
            print "passei"
            result += con.recv(1024)
            print result
        return result

    def customize_msg(self, cmd, pos, buff, size, partition_size):
        new_pos = pos % self.partition_size
        end = min(new_pos + size, partition_size)
        new_size = end - new_pos
        new_buff = buff[:new_size]
        return "#".join(map(str, [cmd, new_pos, new_size, new_buff])), new_size

    def prepare_msg(self, msg):
        cmd, content = msg[:-1].split("(")
        buff = " "
        pos = size = 0

        if cmd == "read":
            pos, size = content.split(',')
        elif cmd == "write":
            pos, buff, size = content.split(',')

        pos = int(pos)
        size = int(size)
        target1 = pos / self.partition_size
        target2 = (pos + size - 1) / self.partition_size
        msgs = []
        mini = 0
        for i in range(target1, target2 + 1):
            if not i == 0:
                mini = (i * self.partition_size) + 1
            maxi = (i + 1) * self.partition_size
            tmp, sent = self.customize_msg(cmd, pos, buff,
                                           size, self.partition_size)
            msgs.append(tmp)
            size -= sent
            buff = buff[sent:]
            pos = 0
        tmp = []
        cmd, pos, size, buff = msgs[0].split('#', 3)
        result = self.send_msg(msgs, self.cons[target1:target2+1])
