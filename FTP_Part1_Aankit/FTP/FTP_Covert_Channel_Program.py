import os   #allows me to access os functions
import stat #interprets from os library

filePermissions = []

#https://stackoverflow.com/questions/1861836/checking-file-permissions-in-linux-with-python
#print(bin(os.stat("/home/xenipulator/Desktop/CYEN 301/Assignments/FTP/ftp.pdf").st_mode))

#create an array to hold names of files in directory
banana = os.listdir("/home/xenipulator/Desktop/CYEN 301/Assignments/FTP")

#print array of files
print (banana)

for i in banana:
    path = "/home/xenipulator/Desktop/CYEN 301/Assignments/FTP/"+i

    filePermissions.append(bin(os.stat(path).st_mode)[8:])  #adds binary representation of permissions 
                                                            #to the file permissions array using the path
                                                            #the [8:] is to isolate the permissions portion

print (filePermissions) #prints array of file permission binary

usethese = []

#this next part goes through the file permissions 
#array and checks the first 3 boolean values
#if the first 3 are not set, then append those in
#the use these array 
for g in filePermissions:
    if(g[:3] == "000"):
        usethese.append(g[3:])

print("\n\n")
print(usethese)

message = ""

for i in usethese:
    n = int(i,2)
    message+=n.to_bytes((n.bit_length() + 6) // 7, 'big').decode()

print(message)