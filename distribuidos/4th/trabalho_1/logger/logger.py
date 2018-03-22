#!/usr/bin/env python
# -*- coding: utf-8 -*-

import socket
from threading import Thread
from managers import MemoryManager, SemaphoreManager

class LoggerServer:

    def __init__(self, port, m_key, s_key):
        self.ip = ''
        self.port = port
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.partition = MemoryManager(m_key)
        self.sem = SemaphoreManager(s_key)

    def backup(self):
        f = open('backup%d.txt' % self.port, 'w')
        self.sem.acquire()
        f.write(self.partition.retrieve())
        self.sem.release()
        f.close()

    def host(self):
        origin = (self.ip, self.port)
        self.sock.bind(origin)
        self.sock.listen(50)
        while True:
            try:
                print "logger online"
                con, client = self.sock.accept()
                print client
                h = Thread(target=self.handle, args=(con,))
                h.start()
            except KeyboardInterrupt:
                self.partition.detach()
                self.sem.delete()
                print "logger será desligado ASAP"
                break;

    def handle(self, con):
        cmd = ""
        tmp = []
        while True:
            try:
                msg = con.recv(5)
                print msg
                if msg == "pls":
                    f = open("backup%d.txt" % self.port)
                    memory = f.read()
                    print memory
                    con.send(memory)
                else:
                    break
            except:
                break


class LoggerClient:

    def __init__(self, m_key, s_key, hosts_path):
        f = open(hosts_path, "r")
        lines = f.readlines()
        self.host_list = lines[0].split(";")
        self.cons = []
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.partition = MemoryManager(m_key)
        self.sem = SemaphoreManager(s_key)

    def establish_connections(self):
        for i, host in enumerate(self.host_list):
            addr, port = host.split(":")
            print 'connecting to', addr, port
            tmp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            tmp.connect((addr, int(port)))
            self.cons.append(tmp)

    def require_backups(self):
        f = open('global_backup.txt', 'w')
        print "opened file"
        self.sem.acquire()
        f.write(self.partition.retrieve())
        self.sem.release()
        print "wrote first part"
        for con in self.cons:
            con.send("pls")
            print "asked for first"
            f.write(con.recv(self.partition.get_size()))
            print "wrote first"
        f.close()
