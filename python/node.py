import socket
import sys
import time


def connectToPeer(host, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))
        #s.sendall(b'hola gente')
        #data = s.recv(1024)
    #print('Received', repr(data))
    return s

def sendVersionMessage(peer):
    version = 1
    services = 1
    timeStamp = int(time.time())
    some_bytes = version.to_bytes(4, sys.byteorder)
    my_bytearray = bytearray(some_bytes)
    my_bytearray.extend(services.to_bytes(8, sys.byteorder))
    my_bytearray.extend(timeStamp.to_bytes(8, sys.byteorder))
    print(my_bytearray)
    print(len(my_bytearray))
    print(time.time())

#Funcion
def main(): 
    HOST = '38.64.140.250'      
    PORT = 8333 
    #peer = connectToPeer(HOST, PORT)
    peer = None
    sendVersionMessage(peer)

main()
