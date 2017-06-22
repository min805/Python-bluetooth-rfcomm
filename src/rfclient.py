#! /usr/bin/python
'''
rfclient.py
Created on Jun 20, 2017
@author: min
'''

import sys
from bluetooth import *

class myClient(object):
    '''For Client '''
    def __init__(self,a_name,a_addr=None):
        #self.first_match
        self.port = None
        self.name = None
        self.host = None
        self.client_sock = None
        self.is_found = "No"
        
        self.myscan(a_name,a_addr)
        #self.myconnect()
        #self.mysend("Sending message from client")
        #self.myreceive()
        #self.mydisconnect()
        
    def __str__(self):
        ret = self.is_found
        return ret       
        
    def myscan(self,_name,_addr):  
        print("Scan device...")
        device_match = find_service(name=_name,address=_addr )

        if len(device_match) == 0:
            print("cannot find the server.")
            self.is_found = "No"
            sys.exit(0)
        else:
            print ("found {} matches".format(len(device_match)) )
            self.is_found = "Yes"
    
        first_match = device_match[0]
        self.port = first_match["port"]
        self.name = first_match["name"]
        self.host = first_match["host"]
        print("connect port:{},name:{},host:{}".format(self.port,self.name,self.host) )

    def myconnect(self):
        print("connecting...")
        self.client_sock=BluetoothSocket(RFCOMM)
        self.client_sock.connect((self.host,self.port))
        print('Okay')
        
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
    myname = "sloanled"
    client_addr = "00:1A:7D:DA:71:08"
    server_addr = "B8:27:EB:97:2B:42"
    
    c = myClient("sloanled")
    print(c)
    c.myconnect()
    c.mysend("Sent message from client.")
    c.myreceive()
    c.mydisconnect()


