#!/usr/bin/env python
# -*- coding: utf-8 -*-

from shared_memory import Server
import sys

if len(sys.argv) == 5:
    sv = Server(int(sys.argv[1]), int(sys.argv[2]),
                int(sys.argv[3]), int(sys.argv[4]))
    sv.serve()
else:
    print len(sys.argv)
    print "Execute o código da seguinte maneira:"
    print "python server.py PORT_NUMBER PARTITION_SIZE M_KEY, S_KEY"
