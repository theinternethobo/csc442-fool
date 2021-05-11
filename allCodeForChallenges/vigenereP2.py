#!/usr/bin/python

import sys
import string

## Global Vars ##
# lowercase alphabet
LowAlp = list(string.ascii_lowercase)

# uppercase alphabet
UpAlp = list(string.ascii_uppercase)

## FUNCTIONS ##
def Encode(text, key):
    # init vars
    textVal = 0
    textIndex = 0
    keyVal = 0
    keyIndex = 0
    strVal = 0
    str_encode = ""

    for i in text:
        if i == "\n":
            return str_encode

        while ((key[keyIndex] not in LowAlp) & (key[keyIndex] not in UpAlp)):
            keyIndex += 1
            if keyIndex == (len(key) - 1):
                keyIndex = 0

        if key[keyIndex] in LowAlp:
            keyVal = LowAlp.index(key[keyIndex])
        elif key[keyIndex] in UpAlp:
            keyVal = UpAlp.index(key[keyIndex])

        if i in LowAlp:
            textVal = LowAlp.index(i)
            strVal = (textVal + keyVal) % 26
            str_encode += LowAlp[strVal]
            if keyIndex == (len(key) - 1):
                keyIndex = 0
            else:
                keyIndex += 1

        elif i in UpAlp:
            textVal = UpAlp.index(i)
            strVal = (textVal + keyVal) % 26
            str_encode += UpAlp[strVal]
            if keyIndex == (len(key) - 1):
                keyIndex = 0
            else:
                keyIndex += 1

        else:
            str_encode += i

    return str_encode

def Decode(text, key):
    # init vars
    textVal = 0
    textIndex = 0
    keyVal = 0
    keyIndex = 0
    strVal = 0
    str_encode = ""

    for i in text:
        if i == "\n":
            return str_encode

        while ((key[keyIndex] not in LowAlp) & (key[keyIndex] not in UpAlp)):
            keyIndex += 1
            if keyIndex == (len(key) - 1):
                keyIndex = 0

        if key[keyIndex] in LowAlp:
            keyVal = LowAlp.index(key[keyIndex])
        elif key[keyIndex] in UpAlp:
            keyVal = UpAlp.index(key[keyIndex])

        if i in LowAlp:
            textVal = LowAlp.index(i)
            strVal = abs(26 + textVal - keyVal) % 26
            str_encode += LowAlp[strVal]
            if keyIndex == (len(key) - 1):
                keyIndex = 0
            else:
                keyIndex += 1

        elif i in UpAlp:
            textVal = UpAlp.index(i)
            strVal = abs(26 + textVal - keyVal) % 26
            str_encode += UpAlp[strVal]
            if keyIndex == (len(key) - 1):
                keyIndex = 0
            else:
                keyIndex += 1

        else:
            str_encode += i

    return str_encode

## MAIN ##
# checking if user input allowable flags
if (sys.argv[1] != "-e") & (sys.argv[1] != "-d"):
    print "ERROR: Invalid flag"
    sys.exit()

# check if key is given
try:
    if (sys.argv[2] == "") | (sys.argv[2] == "\n"):
        print "ERROR: Invalid key input"
        sys.exit()

# catch error and display that no key is given
except IndexError:
    print "ERROR: No key given"
    sys.exit()

# the actual start of the program
# declare the flag and the key for encode/decode
flag = sys.argv[1]
key = sys.argv[2]

# loop program
while(1):
    # take input from user
    try:
        text = raw_input('')

    except EOFError:
        sys.exit()

    # encode or decode the text???
    if flag == "-e":
        print Encode(text, key)

    elif flag == "-d":
        print Decode(text, key)
