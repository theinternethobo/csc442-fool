import os   #allows me to access os functions
import stat #interprets from os library

Method = True#if true, 7 bit, else 10 bit
filePermissions = []

#https://stackoverflow.com/questions/1861836/checking-file-permissions-in-linux-with-python
#print(bin(os.stat("/home/xenipulator/Desktop/CYEN 301/Assignments/FTP/ftp.pdf").st_mode))

#create an array to hold names of files in directory
banana = os.listdir("/home/xenipulator/Desktop/CYEN 301/Assignments/FTP")
usethese = []

#print array of files
print (banana)

if(Method):
    for i in banana:
        path = "/home/xenipulator/Desktop/CYEN 301/Assignments/FTP/"+i

        filePermissions.append(bin(os.stat(path).st_mode)[8:])  #adds binary representation of permissions 
                                                                #to the file permissions array using the path
                                                                #the [8:] is to isolate to the final 8 bits
        #this next part goes through the file permissions 
        #array and checks the first 3 boolean values
        #if the first 3 are not set, then append those in
        #the use these array 
        for g in filePermissions:
            if(g[:3] == "000"):
                usethese.append(g[3:])

if(!Method):
    for i in banana:
        path = "/home/xenipulator/Desktop/CYEN 301/Assignments/FTP/"+i

        filePermissions.append(bin(os.stat(path).st_mode)[6:])  #adds binary representation of permissions 
                                                                #to the file permissions array using the path
                                                                #the [6:] is to isolate to the final 10 bits
        for g in filePermissions:
            usethese.append(g)

print (filePermissions) #prints array of file permission binary


print("\n\n")
print(usethese)

message = ""

#gotta edit lines after this for the 10 bit, prolly add an if statement
for i in usethese:
    n = int(i,2)
    message+=n.to_bytes((n.bit_length() + 6) // 7, 'big').decode()

print(message)