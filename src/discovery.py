'''
Created on Jun 22, 2017
@author: root
'''

from bluetooth import *
#import bluetooth

class MyDiscovery(object):

    def __init__(self):
        self.name = 'raspberrypi'        
        self.addr = None
        self.channel = None
        self.protocol = None
        self.client_socket = None
        self.server_socket = None
        
    def my_discovery(self,_name):
        print("My Discovery")
        print("find device by name {}".format(_name))
        self.name = _name
        nearby = discover_devices()
        for bdaddr in nearby:
            print("Address:{}, name:{}".format(bdaddr,lookup_name(bdaddr)))
            if _name == lookup_name(bdaddr):
                self.addr = bdaddr
                break
        if self.addr is not None:
            print("....found addr:",self.addr)
        else:
            print("....Cannot found.")    
    
    
        
    def my_scan(self,_name=None,_uuid=None,_addr=None):  
        print("My Scan")
        print("Scan device...")
        device_match = find_service(name=_name,uuid=_uuid,address=_addr )
        
        if len(device_match) == 0:
            print("cannot find the server.")
            print ("Exit application")
            sys.exit(0)
        else:
            print ("found {} matches".format(len(device_match)) )
        
        first_match = device_match[0]
        #print (first_match)
        self.protocol=first_match["protocol"]
        self.channel = first_match["port"]
        self.name = first_match["name"]
        self.addr = first_match["host"]
        print("try to connect: protocol:{},channel:{},name:{},addr:{}".format(self.protocol,self.channel,self.name,self.addr) )
       
        #for match in device_match:
        #    #print(match)
        #    self.protocol = match["protocol"]
        #    self.channel = match["port"]
        #    self.name = match["name"]
        #    self.addr = match["host"]
        #    print("connect protocol:{},channel:{},name:{},addr:{}".format(self.protocol,self.channel,self.name,self.addr) )
        #    #if self.name == "Generic Access Profile" :
        #    #    break

    def my_connect(self):
        print("connecting...")
        sys.stdout.flush()
        self.client_socket = BluetoothSocket(RFCOMM)
        self.client_socket.connect((self.addr,self.channel))
        print("Okay")
        
    def my_disconnect(self):        
        self.client_socket.close() 
        print("disconnect.")  
  
    def my_send(self,message):   
        self.client_socket.send(message)
        print("sent message.")
        
    def my_receive(self):    
        data = self.client_socket.recv(80)
        print ("received:", data)    

if __name__ == '__main__':
    myname = "raspberrypi"
    myuuid = "11111111-2222-3333-4444-555555555555"
    #client_addr = "00:1A:7D:DA:71:08"
    #server_addr = "B8:27:EB:97:2B:42"
    
    d = MyDiscovery()
    #d.my_discovery(myname)
    d.my_scan(_name=myname)
    d.my_connect()
    d.my_send("sending from client.")
    d.my_receive()
    d.my_disconnect()
    



        