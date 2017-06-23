#! /usr/bin/python
'''
rfserver.py
Created on Jun 20, 2017
@author: min
'''

import sys
from bluetooth import *


class myServer(object):
    
    def __init__(self):
        self.client_sock = None
        #self.client_info = None
        self.server_sock = BluetoothSocket(RFCOMM)        
        #self.server_sock.bind( ("B8:27:EB:97:2B:42",PORT_ANY) )
        self.server_sock.bind( ("",PORT_ANY) )
        self.server_sock.listen(1)
        
        
    def getserverinfo(self):    
        server_addr,server_port = self.server_sock.getsockname() 
        print ("server addr={}, channel={}".format(server_addr,server_port))
 
        
    def myadvertising(self,a_name,a_uuid):  
        
        print("start advertising...")    
        advertise_service(self.server_sock,name=a_name,
                          service_id = a_uuid,
                          service_classes = [a_uuid,SERIAL_PORT_CLASS],
                          profiles=[SERIAL_PORT_PROFILE],
                          description="myAdvertising")
        
        #self.client_sock,client_info = self.server_sock.accept()
        #print("accepted connection form", client_info)
        
        try:
            self.server_sock.settimeout(10.0)
            self.client_sock,client_info = self.server_sock.accept()
            print("accepted connection form", client_info)
        except Exception, e: 
            print ("Exception.{}".format(e))
            print ("Exit application")             
            sys.exit(0)   
            
    def mysend(self,message):
        self.client_sock.send(message)
        print("sent message")
        
    def myreceive(self):    
        data = self.client_sock.recv[1024]
        print("received: ",data)

    def disconnect(self):
        self.client_sock.close()
        self.server_sock.close()

if __name__ == '__main__':
    myname = "sloanled"
    myuuid = "11111111-2222-3333-4444-555555555555"
    client_addr = "00:1A:7D:DA:71:08"
    server_addr = "B8:27:EB:97:2B:42"
    
    s=myServer()
    s.getserverinfo()
    s.myadvertising(myname,myuuid)
    s.mysend("sent message from server.")
    s.myreceive()
    s.disconnect()




