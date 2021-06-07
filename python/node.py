import socket
import sys
import time

BYTEORDER = 'big'

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
    my_bytearray = bytearray(version.to_bytes(4, BYTEORDER))
    my_bytearray.extend(services.to_bytes(8, BYTEORDER))
    my_bytearray.extend(timeStamp.to_bytes(8, BYTEORDER))
    print(my_bytearray)
    print(len(my_bytearray))
    print(time.time())


def stringToIP(ip):
    res = bytearray([0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0xFF, 0xFF])
    ip_array = ip.split('.')
    for x in ip_array:
        res.extend(int(x).to_bytes(1, 'big'))
    return res


def address(services, ip, port):
    my_bytearray = bytearray(services.to_bytes(8, BYTEORDER))
    my_bytearray.extend(ip)
    my_bytearray.extend(port.to_bytes(2, BYTEORDER))
    return my_bytearray


#Funcion
def main():
    HOST = '38.64.140.250'
    PORT = 8333
    #peer = connectToPeer(HOST, PORT)
    peer = None
    sendVersionMessage(peer)


main()
