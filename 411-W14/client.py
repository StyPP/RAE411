import os
from socket import *

"""
Functions
"""
def mult(A, B):
    C, n, m, p = [], len(A), len(A[0]), len(B[0])
    for i in range(n):
        line = []
        for j in range(p):
            summ = 0
            for k in range(m):
                summ += A[i][k]*B[k][j]
            line.append(summ)
        C.append(line)
    return C

def StrToMtr(string):
    N = []
    for elt in string.split(";"):
        O = []
        elt = elt.split(",")
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

"""
Execution
"""

# recieve message
host = "192.168.43.19"
port = 6678
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
os._exit(0)

#-------------
#compute matrix
L = []
for m in data.split('!'):
    L.append(StrToMtr(m))
string = MatToStr(mult(L[0],L[1]))

#--------------
# Return message
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
