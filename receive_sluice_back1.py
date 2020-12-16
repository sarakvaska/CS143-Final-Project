#!/usr/bin/env python
import sys
import struct
import os
import socket
import time

DPORT = 1235
srcPort = 1234

# dict where keys are port numbers, values are priorities (priority 1 = highest)
# zoom, skype, email, netflix, hulu
# zoom, skype, and email: high priorty, netflix and hulu: low priority
# host 2 is our middle host which is determining where to send traffic
app_type_to_download = {1: 1000, 2: 4000, 3: 10, 4: 3000, 5: 3000}
app_type_to_priority = {1: 1, 2: 1, 3: 2, 4: 3, 5: 3}
app_type_to_name = {0: 'User App', 1: 'Zoom', 2: 'Skype', 3: 'Email', 4: 'Netflix', 5: 'Hulu'}

def main():
    while True:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.bind(('', DPORT))
        data, clientAddress = s.recvfrom(200)
        app_type, = struct.unpack('>I', data)
        print str("App Type: ", app_type), str("Host Address: ", clientAddress), str("App Type Name: ", app_type_to_name[app_type])

        s1 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s1.bind(('', srcPort))
        data1 = struct.pack('>I', 0)
        # have dictionary that maps app type with host
        time_delay = 1/app_type_to_upload[app_type]*app_type_to_priority[app_type]
        time.sleep(time_delay)
        s1.sendto(data1, ('10.0.0.2', DPORT))

if __name__ == '__main__':
    main()
