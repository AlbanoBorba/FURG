#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sysv_ipc

class MemoryManager:

    def __init__(self, key, size=7):
        self.size = size
        try:
            self.mem = sysv_ipc.SharedMemory(key)
        except sysv_ipc.ExistentialError:
            self.mem = sysv_ipc.SharedMemory(key, sysv_ipc.IPC_CREAT,
                                             0666, size)
            self.mem.write("."[0]*size, 0)

    def write(self, position, buff):
        self.mem.write(buff, position)
        return "ok"

    def read(self, position, size):
        return self.mem.read(size, position)

    def retrieve(self):
        buff = self.mem.read(self.size).split()
        print buff
        memory = ""
        for element in buff:
            memory += element
        return memory

    def delete(self):
        self.mem.remove()

    def detach(self):
        self.mem.detach()

    def get_size(self):
        return self.mem.size


class SemaphoreManager:

    def __init__(self, key):
        try:
            self.sem = sysv_ipc.Semaphore(key)
            print "already exists"
        except sysv_ipc.ExistentialError:
            self.sem = sysv_ipc.Semaphore(key, sysv_ipc.IPC_CREAT, 0666, 1)
            print "created"

    def acquire(self):
        self.sem.acquire(timeout=2)

    def release(self):
        self.sem.release()

    def delete(self):
        try:
            self.sem.remove()
        except sysv_ipc.ExistentialError:
            print "already removed"
