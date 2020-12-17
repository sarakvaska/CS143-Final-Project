
#!/usr/bin/env python
import sys
import struct
import os
import socket
import time

DPORT = 1234
# DPORT = 0x56ce

app_type_to_bandwidth = {1: 800, 2: 512, 3: 10, 4: 10, 5: 10}
app_type_to_priority = {1: 1, 2: 1, 3: 2, 4: 3, 5: 3}
app_type_to_name = {0: 'User App', 1: 'Zoom', 2: 'Skype', 3: 'Email', 4: 'Netflix', 5: 'Hulu'}
app_type_to_host = {0: '10.0.0.1', 1: '10.0.0.3', 2: '10.0.0.4', 3: '10.0.0.5', 4: '10.0.0.6', 5: '10.0.0.7'}

def main():
     while True:
         s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
         s.bind(('', DPORT))
         data, clientAddress = s.recvfrom(200)
         app_type, = struct.unpack('>I', data)

         print "App Type: ", str(app_type), "Host Address: ",  str(clientAddress), "App Type Name: ", str( app_type_to_name[app_type])

         if(app_type != 0):
             time_delay = 1/app_type_to_bandwidth[app_type]*(app_type_to_priority[app_type]**2)
             time.sleep(time_delay)
         data1 = struct.pack('>I', app_type)
         s.sendto(data1, (app_type_to_host[app_type], DPORT))

if __name__ == '__main__':
    main()
