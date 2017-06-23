#! /usr/bin/python
'''
rfclient.py
Created on Jun 20, 2017
@author: min
'''

import sys
#import bluetooth
from bluetooth import *

class myClient(object):
    '''For Client '''
    def __init__(self):
        #self.first_match
        self.port = 1
        self.name = ""
        self.addr = ""
        self.client_sock = None
        
        #self.myscan(a_name,a_addr)
        #self.myconnect()
        #self.mysend("Sending message from client")
        #self.myreceive()
        #self.mydisconnect()
        
    #def __str__(self):
    #    ret = self.is_found
    #    return ret       
        
    def mydiscovery(self):
        self.name = 'raspberrypi'        
        self.addr = None
        print("find device by name {}".format(self.name))
        nearby = discover_devices()
        for bdaddr in nearby:
            if self.name == lookup_name(bdaddr):
                self.addr = bdaddr
                break
        if self.addr is not None:
            print("....found addr:",self.addr)
        else:
            print("....Cannot found.")    
    
    
        
    def myscan(self,_name=None,_uuid=None,_addr=None):  
        print("Scan device...")
        device_match = find_service(name=_name,uuid=_uuid,address=_addr )
        #device_match = find_service(name=_name,uuid=SERIAL_PORT_CLASS )

        if len(device_match) == 0:
            print("cannot find the server.")
            print ("Exit application")
            sys.exit(0)
        else:
            print ("found {} matches".format(len(device_match)) )
       
    
        first_match = device_match[0]
        print (first_match)
      
        self.port = first_match["port"]
        self.name = first_match["name"]
        self.addr = first_match["host"]
        print("connect channel:{},name:{},addr:{}".format(self.port,self.name,self.addr) )

    def myconnect(self,_addr=None):
        print("connecting...")
        self.client_sock=BluetoothSocket(RFCOMM)
        #try:
        #    self.client_sock.settimeout(10.0)
        #    if _addr == None:
        #        self.client_sock.connect((self.addr,self.port))
        #    else:    
        #        self.client_sock.connect((_addr,1))
        #        
        #except Exception, e: 
        #    print ("Exception.{}".format(e))
        #    print ("Exit application")             
        #    sys.exit(0)   
        
        self.client_sock.connect((self.addr,self.port))
        
        print('...Okay')    
        
    def mysend(self,message):   
        self.client_sock.send(message)
        print("sent message.")
        
    def myreceive(self):    
        data = self.client_sock.recv(80)
        print ("received:", data)

    def mydisconnect(self):
        print("disconnect.")
        self.client_sock.close()


if __name__ == '__main__':
    myname = "raspberrypi"
    myuuid = "11111111-2222-3333-4444-555555555555"
    client_addr = "00:1A:7D:DA:71:08"
    server_addr = "B8:27:EB:97:2B:42"

    
    c = myClient()
    #print(c)
    #c.myscan(_name=myname,_uuid=myuuid,_addr=server_addr)
    #c.myscan(_addr=server_addr)
    #c.myscan(_name=myname)
    
    c.mydiscovery()
    #c.myconnect(server_addr)
    c.myconnect(c.addr)
    c.mysend("Sent message from client.")
    c.myreceive()
    c.mydisconnect()


