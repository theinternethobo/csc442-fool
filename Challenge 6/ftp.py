#Names: Jerome Reed, David Amort , Jared Andra , Josh Iselin , Tim Huhn , Ibrahim Al-Agha

# use Python 3
  
from ftplib import FTP

# FTP server details
IP = "138.47.99.163"
PORT = 21
USER = "salt"
PASSWORD = "tlas"
FOLDER = "~/FILES"
USE_PASSIVE = True # set to False if the connection times out

# connect and login to the FTP server
ftp = FTP()
ftp.connect(IP, PORT)
ftp.login(USER, PASSWORD)
ftp.set_pasv(USE_PASSIVE)

# navigate to the specified directory and list files
ftp.cwd(FOLDER)
files = []
ftp.dir(files.append)

for i in files:
    ftp.mget[i]

# exit the FTP server
ftp.quit()

#7 bit method
def SevenBitMethod(line):
    permission = line[0:10]
    if permission[0:3] != '---':
        return
    else:
        octet1 = permission[1:4]
        octet2 = permission[4:7]
        octet3 = permission[7:10]
        octet1 = octet1.replace('-','0')
        octet2 = octet2.replace('-','0')
        octet3 = octet3.replace('-','0')
        for c in octet1:
            try:
                int(c)
            except(ValueError):
                octet1 = octet1.replace(c,'1')
        for c in octet2:
            try:
                int(c)
            except(ValueError):
                octet2 = octet2.replace(c,'1')
        for c in octet3:
            try:
                int(c)
            except(ValueError):
                octet3 = octet3.replace(c,'1')
        value = ''
        value+=octet1
        value+=octet2
        value+=octet3
        return chr(int(value,2))

#10 bit method
def TenBitMethod(line):
    permission = line[0:10]
    permission = permission.replace('-','0')
    for c in permission:
        try:
            int(c)
        except(ValueError):
            permission = permission.replace(c,'1')
    return permission

def binaryDecoder(binaryString):
    string = ''
    a = 0
    while(True):
        b = a + 7
        binary = binaryString[a:b]
        if binary == '':
            break
        deci = int(binary,2)
        string += chr(deci)
        a = b 
    print(string)

###MAIN###
message = ''
if FOLDER == '/7/':
        for f in files:
            try:
                print(f)
            except(TypeError):
                continue
        print(message)
else:
        for f in files:
            print(f)
        binaryDecoder(message)        
