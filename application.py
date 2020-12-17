import sys
import struct
import os
import socket
import time

PORT = 1234

# Dictionary linking app type code to required user download bandwidth for quality service (Kbps)
app_type_to_download_bandwidth = {1: 1000, 2: 4000, 3: 10, 4: 3000, 5: 3000}

# Dictionary linking app type code to priority, with highest priority being 1 and lowest priority being 3
app_type_to_priority = {1: 1, 2: 1, 3: 2, 4: 3, 5: 3}

# Dictionary linking app type code to app name
app_type_to_name = {0: 'User App', 1: 'Zoom', 2: 'Skype', 3: 'Email', 4: 'Netflix', 5: 'Hulu'}

def main():
    while True:
        
        # Receive incoming packets (representing user uploading to app)
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.bind(('', PORT))
        data, clientAddress = s.recvfrom(200)
        app_type, = struct.unpack('>I', data)
        print "App Type:", str(app_type), "Client Address:", str(clientAddress), "App Type Name:", app_type_to_name[app_type]

        # Send outgoing response packet (representing user downloading from app)
        data1 = struct.pack('>I', 0)
        time_delay = 1 / app_type_to_download_bandwidth[app_type] * (app_type_to_priority[app_type]**2)
        time.sleep(time_delay)
        s.sendto(data1, ('10.0.0.2', PORT))

if __name__ == '__main__':
    main()
