#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
import sys
from threading import Thread
from logger import LoggerServer


if len(sys.argv) == 4:
    logger = LoggerServer(int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]))
    lg = Thread(target=logger.host, args=())
    lg.start()
    while True:
        try:
            time.sleep(15)
            print "making backup at", \
                  time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
            logger.backup()
        except KeyboardInterrupt:
            print "xau"
            break
else:
    print len(sys.argv)
    print "Execute o código da seguinte maneira:"
    print "python logger_sv.py PORT_NUMBER M_KEY S_KEY"
