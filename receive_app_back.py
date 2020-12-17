#!/usr/bin/env python
import sys
import struct
import os
import socket
import time

DPORT = 1234
# DPORT = 0x56ce

app_type_to_download = {1: 1000, 2: 4000, 3: 10, 4: 3000, 5: 3000}
app_type_to_priority = {1: 1, 2: 1, 3: 2, 4: 3, 5: 3}
app_type_to_name = {0: 'User App', 1: 'Zoom', 2: 'Skype', 3: 'Email', 4: 'Netflix', 5: 'Hulu'}

def main():
    while True:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.bind(('', DPORT))
        data, clientAddress = s.recvfrom(200)
        app_type, = struct.unpack('>I', data)
        print "App Type:", str(app_type), "Host Address:", str(clientAddress), "App Type Name:", app_type_to_name[app_type]

        data1 = struct.pack('>I', 0)
        # have dictionary that maps app type with host
        time_delay = 1/app_type_to_download[app_type]*(app_type_to_priority[app_type]**2)
        time.sleep(time_delay)
        s.sendto(data1, ('10.0.0.2', DPORT))

if __name__ == '__main__':
    main()
