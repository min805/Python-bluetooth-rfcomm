#! /usr/bin/python
'''
Created on Jun 20, 2017
@author: min
'''

import sys
from bluetooth import *

server_sock=BluetoothSocket(RFCOMM)
server_sock.bind(("",PORT_ANY))
localaddr,localport = server_sock.getsockname()
server_sock.listen(1)

advertise_service(server_sock,name="sloanled",service_classes=[SERIAL_PORT_CLASS],profiles=[SERIAL_PORT_PROFILE])

client_sock,client_info = server_sock.accept()
print("accepted connection form", client_info)

client_sock.send("pyBluez server sent")
data = client_sock.recv[1024]
print("received: ",data)

client_sock.close()
server_sock.close()