'''
Created on Jun 23, 2017
@author: root
'''
import sys
import re
from bluetooth import *

import subprocess


class MyAdvertising(object):
    
    def __init__(self):
        self.client_socket = None
        self.client_info = None   
        
        self.sever_addr = subprocess.check_output("hcitool dev | grep hci",shell=True).replace('hci0',"").strip()
        print("my_bdaddr:{}".format(self.sever_addr)) 
  
        self.server_socket = BluetoothSocket(RFCOMM)        
        self.server_socket.bind( (self.sever_addr,PORT_ANY) )
        print("listen RFCOMM connection")
        self.server_socket.listen(1) 
        self.server_socket.settimeout(20)       
  
        
        
    def my_accept(self):
        try:
            self.client_socket,self.client_info = self.server_socket.accept()
            print("Accepted connect: {}".format(self.client_info))
        except Exception,e:
            print("Exception:{}".format(e))
            sys.exit(0)
            
    def get_serverinfo(self):    
        server_addr,server_port = self.server_socket.getsockname() 
        print ("server addr={}, channel={}".format(server_addr,server_port))
 
        
    def my_advertising(self,a_name,a_uuid): 
        print("start advertising...")    
        advertise_service(self.server_socket,name=a_name,
                          service_id = a_uuid,
                          service_classes = [a_uuid,SERIAL_PORT_CLASS],
                          profiles=[SERIAL_PORT_PROFILE],
                          description="myAdvertising")
    
    def my_send(self,message):
        self.client_socket.send(message)
        print("sent message")
        
    def my_receive(self):    
        data = self.client_socket.recv(80)
        print("received: {}".format(data))

    def my_disconnect(self):
        self.client_socket.close()
        self.server_socket.close()
        print("disconnect.")

if __name__ == '__main__':
    myname = "raspberrypi"
    myuuid = "11111111-2222-3333-4444-555555555555"
    #client_addr = "00:1A:7D:DA:71:08"
    #server_addr = "B8:27:EB:97:2B:42"
    
    s=MyAdvertising()
    s.get_serverinfo()
    s.my_advertising(myname,myuuid)
    s.my_accept()
    s.my_send("sent message from server.")
    s.my_receive()
    s.my_disconnect()
    
    