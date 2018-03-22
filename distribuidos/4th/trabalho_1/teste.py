#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sysv_ipc
import time

key = 52

try:
    sem = sysv_ipc.Semaphore(key)
    print "already exists"
except sysv_ipc.ExistentialError:
    sem = sysv_ipc.Semaphore(key, sysv_ipc.IPC_CREAT, 0666, 1)
    print "created"

sem.acquire()
print "entrei"
time.sleep(10)
sem.release()
print "sai"
