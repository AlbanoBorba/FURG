#!/usr/bin/env python
# -*- coding: utf-8 -*-

from shared_memory import Client

cl = Client("setup.txt")

command = ""
cl.establish_connections()
while True:
    try:
        command = raw_input('Digite o comando a ser executado.\n')
    except KeyboardInterrupt:
        print 'Adeus'
        break
    if not command == "quit":
        result = cl.prepare_msg(command)
    else:
        break
