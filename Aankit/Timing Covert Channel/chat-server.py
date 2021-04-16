import socket
from time import sleep

port = 1337

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("", port))#binding to no specific ip, but port 1337
s.listen(0)#listen

print("Server is listening")

#c = new socket used for comm
#addr = address of client
c, addr = s.accept()

b = [] 

msg = "Some message Is cool and I am A Cyber Major, I like math, and i am good at it,\n"
for i in "abcdef":
    b.append(bin(ord(i))[2:].zfill(8))

covert = ""

h = 0
for i in b:
    for d in b[h]:
        covert += "" + d
    h+=1

g = 0
#Send encoded message
for i in msg:
    c.send(i.encode())
    if(g != (len(covert)) and covert[g] == "1"):
        sleep(.01)

    elif(g != (len(covert)) and covert[g] == "0"):
        sleep(.02)

    if(g == (len(covert))):
        sleep (.03)
        print(i)

    if(g != (len(covert))):
        g += 1

    
    
    

c.send("EOF".encode())#send EOF

print ("Message sent")

c.close()#closes second socket