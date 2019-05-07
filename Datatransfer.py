
#as server.py 
# Message Receiver
import os
from socket import *

host = "192.168.43.105"
port = 6677
buf = 1024
addr = (host, port)
UDPSock = socket(AF_INET, SOCK_DGRAM)
UDPSock.bind(addr)
print ("Waiting to receive messages...")
while True:
    (data, addr) = UDPSock.recvfrom(buf)
    data = data.decode()
    print(data)
    break
UDPSock.close()

#compute matrix
L = []
M = data.split('!')

for m in M:
    N = []
    m = m.split(';')
    for elt in m:
        O = []
        elt = elt.split(',')
        for e in elt:
            O.append(int(e))
        N.append(O)
    L.append(N)

print(L)

def RowToStr(row):
    string = ""
    length = len(row)
    for i in range(length - 1):
        string += str(row[i]) + ","
    string += str(row[length - 1])
    return string

def MatToStr(mat):
    string = ""
    lengthRow = len(mat)
    for i in range(lengthRow - 1):
        string += RowToStr(mat[i]) + ";"
    string += RowToStr(mat[lengthRow - 1])
    return string

string = MatToStr(L[0]) + "!" + MatToStr(L[1])


# Save as client.py 
# Message Sender
host = "192.168.43.19" # set to IP address of target computer
port = 6677
addr = (host, port)
UDPSock = socket(AF_INET, SOCK_DGRAM)
while True:
    #data = input("Enter a message:   ")
    data = string
    data = data.encode()
    UDPSock.sendto(data, addr)
    if data == "exit":
        break
UDPSock.close()
os._exit(0)


