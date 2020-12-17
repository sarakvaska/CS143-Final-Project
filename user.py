import argparse
import sys
import socket
import random
import struct
import re
import readline
import numpy as np
import time

PORT = 1234

# Dictionary linking app type code to app name
app_type_to_name = {0: 'User App', 1: 'Zoom', 2: 'Skype', 3: 'Email', 4: 'Netflix', 5: 'Hulu'}

def main():

    if len(sys.argv)<2:
        print 'pass 1 argument: <app_type>'
        exit(1)

    addr = socket.gethostbyname(10.0.0.2)
    app_type = int(sys.argv[2])

    # Send packet to application through intermediary (representing user uploading to app)
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind(('', PORT))
    data = struct.pack('>I', app_type)
    s.sendto(data, (addr, PORT))
    
    # Receive incoming packets (representing user downloading from app)
    while True:
        data1, clientAddress = s.recvfrom(200)
        app_type, = struct.unpack('>I', data1)
        print "App Type:", str(app_type), "Host Address:", str(clientAddress), "App Type Name:", app_type_to_name[app_type]

if __name__ == '__main__':
    main()
