import os
from socket import *

def StrToMtr(string):
    N = []
    for elt in string.split(";"):
        O = []
        elt = elt.split(',')
        for e in elt:
            O.append(int(e))
        N.append(O)
    return N

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

mat1 = [[1, 2, 3], [1, 2, 3], [1, 2, 3]]
mat2 = [[1], [2], [3]]

string = MatToStr(mat1) + "!" + MatToStr(mat2)

"""
Execution
"""

#-------------------
# send message
host = "192.168.43.19" # set to IP address of target computer
port = 6678
addr = (host, port)
UDPSock = socket(AF_INET, SOCK_DGRAM)
while True:
    input("press enter to send")
    data = string.encode()
    UDPSock.sendto(data, addr)
    break
UDPSock.close()   

#----------------- 
# Recieve message
host = "192.168.43.19"
port = 6677
buf = 1024
addr = (host, port)
UDPSock = socket(AF_INET, SOCK_DGRAM)
UDPSock.bind(addr)
print("Waiting to receive messages...")
while True:
    (data, addr) = UDPSock.recvfrom(buf)
    data = data.decode()
    break
UDPSock.close()

#---------------
#process response
L = []
for m in data.split("!"):
    L.append(StrToMtr(m))
print(L)


os._exit(0)

