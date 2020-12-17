#!/usr/bin/env python

import argparse
import sys
import socket
import random
import struct
import re
import readline
import numpy as np
import time

DPORT = 1234 # MY_PORT 0x04d2
app_type_to_name = {0: 'User App', 1: 'Zoom', 2: 'Skype', 3: 'Email', 4: 'Netflix', 5: 'Hulu'}

def main():

    if len(sys.argv)<4:
        print 'pass 3 arguments: <destination IP> <srcPort> <app_type>'
        exit(1)

    addr = socket.gethostbyname(sys.argv[1])
    srcPort = int(sys.argv[2])
    app_type = int(sys.argv[3])

    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind(('', srcPort))
    # app_type = application type (zoom, skype, email, netflix, hulu)
    data = struct.pack('>I', app_type)
    s.sendto(data, (addr, DPORT))

    while True:
        data1, clientAddress = s.recvfrom(200)
        app_type, = struct.unpack('>I', data1)
        print "App Type:", str(app_type), "Host Address:", str(clientAddress), "App Type Name:", app_type_to_name[app_type]


if __name__ == '__main__':
    main()
