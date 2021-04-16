import socket
from sys import stdout
from time import time

DEBUG = True

ip = "138.47.102.120"
port = 31337 #same port as the server

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)#create a socket for client

s.connect((ip, port))#connect to specific ip and provide port #

data = s.recv(4096).decode() #recieve message and decode

timing = []

#recieves (without newline) all data until EOF message
while(data.rstrip("\n") != "EOF"):

    #writes directly to console without buffers from print function 
    #stdout.write(data)

    stdout.flush()#flush stdout
    t0 = time()#gets curr time
    data = s.recv(4096).decode() #recieve message and decode
    t1 = time()#gets curr time
    delta = round(t1 - t0,3) #finds diff between times
    timing.append(delta)

    if(DEBUG):
        stdout.write(" {}\n".format(delta))
        stdout.flush()

s.close()#close socket

covert_Message = ""

print("what timing do you want for : ")
zeroTime = float(input("0 : "))
oneTime = float(input("1 : "))

for g in timing:
    if(g != .75):
        if(g <= (zeroTime+.002) and g >= (zeroTime-.002)):
            covert_Message += "0"
        elif(g <= (oneTime+.002) and g >= (oneTime-.002)):
            covert_Message += "1"

print(covert_Message)
message = ""

a = [covert_Message[i:i+8] for i in range(0, len(covert_Message), 8)] #string splitter
for x in a:
    n = int(x,2)
    message+=n.to_bytes((n.bit_length() + 7) // 8, 'big').decode() #From stack overflow https://stackoverflow.com/questions/7396849/convert-binary-to-ascii-and-vice-versa
    
print(message)