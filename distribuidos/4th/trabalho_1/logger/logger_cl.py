#!/usr/bin/env python
# -*- coding: utf-8 -*-
import time
import sys

from logger import LoggerClient

if len(sys.argv) == 3:
    logger = LoggerClient(int(sys.argv[1]), int(sys.argv[2]), "lsetup.txt")
    logger.establish_connections()
    while True:
        time.sleep(30)
        print "making global backup at", \
              time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        logger.require_backups()
else:
    print len(sys.argv)
    print "Execute o código da seguinte maneira:"
    print "python logger_cl.py M_KEY S_KEY"
