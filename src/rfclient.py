#! /usr/bin/python
'''
rfclient.py
Created on Jun 20, 2017
@author: min
'''

import sys
from bluetooth import *


service_match = find_service(name="sloanled")

if len(service_match) == 0:
    print("cannot find the server.")
    sys.exit(0)
    
first_match = service_match[0]
port = first_match["port"]
name = first_match["name"]
host = first_match["host"]

print("connect to ", host)

sock=BluetoothSocket(RFCOMM)
sock.connect((host,port))
sock.send("pyBluz Client sent")
data = sock.recv(80)

print ("received:", data)
sock.close()