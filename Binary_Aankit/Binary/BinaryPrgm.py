import sys
import binascii

def bits2string(b=None):
    return ''.join([chr(int(x, 2)) for x in b])

for line in sys.stdin:

    input = line.rstrip()    
    if 'exit' == input:
        break
    print(f'Length : {len(input)}')
    
    message =""
    #InsertedUsing VIM
    #print((len(input)%8))
    #print((len(input)%7))    

    #String splitter: https://stackoverflow.com/questions/9475241/split-string-every-nth-character

    if((len(input)%8) == 0):
        print("8-bit ASCII\n")
        a = [input[i:i+8] for i in range(0, len(input), 8)] #string splitter
        for x in a:
            n = int(x,2)
            message+=n.to_bytes((n.bit_length() + 7) // 8, 'big').decode() #From stack overflow https://stackoverflow.com/questions/7396849/convert-binary-to-ascii-and-vice-versa
            
        print(message)
        print("\n")
        #inserted using nano

    if((len(input)%7) == 0):
        print("7-bit ASCII\n")
        a = [input[i:i+7] for i in range(0, len(input), 7)]#string splitter

        for x in a:
            n = int(x,2)
            message+=n.to_bytes((n.bit_length() + 6) // 7, 'big').decode() #From stack overflow https://stackoverflow.com/questions/7396849/convert-binary-to-ascii-and-vice-versa
            
        print(message)
        print("\n")

    else:
        print("\n")
        
    
print("Exit")
