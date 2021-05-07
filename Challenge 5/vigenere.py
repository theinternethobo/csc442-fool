#!/usr/bin/env python3

####################################
# Timothy Huhn (The Fool - CYEN 301)
# 3/28/2021
# Vigenere Cipher
####################################

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

    # go thru each letter in the plaintext
    for i in text:

        if i == "\n":
            return str_encode
        
        # ignore anything but letters in the key
        while ((key[keyIndex] not in LowAlp) & (key[keyIndex] not in UpAlp)):
            keyIndex += 1
            if keyIndex == (len(key) - 1):
                keyIndex = 0

        # get the key value on the respective case type
        if key[keyIndex] in LowAlp:
            keyVal = LowAlp.index(key[keyIndex])
        elif key[keyIndex] in UpAlp:
            keyVal = UpAlp.index(key[keyIndex])

        # if the letter in the plaintext is lowercase
        if i in LowAlp:
            textVal = LowAlp.index(i)
            strVal = (textVal + keyVal) % 26
            str_encode += LowAlp[strVal]
            if keyIndex == (len(key) - 1):
                keyIndex = 0
            else:
                keyIndex += 1

        # if the letter in the plaintext is uppercase
        elif i in UpAlp:
            textVal = UpAlp.index(i)
            strVal = (textVal + keyVal) % 26
            str_encode += UpAlp[strVal]
            if keyIndex == (len(key) - 1):
                keyIndex = 0
            else:
                keyIndex += 1

        # if there wasn't a letter in the plaintext
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
    str_decode = ""

    # go thru each letter in the ciphertext
    for i in text:
        if i == "\n":
            return str_decode

        # ignore anything but letters in the key
        while ((key[keyIndex] not in LowAlp) & (key[keyIndex] not in UpAlp)):
            keyIndex += 1
            if keyIndex == (len(key) - 1):
                keyIndex = 0

        # get the key value on the respective case type
        if key[keyIndex] in LowAlp:
            keyVal = LowAlp.index(key[keyIndex])
        elif key[keyIndex] in UpAlp:
            keyVal = UpAlp.index(key[keyIndex])

        # if the letter in the ciphertext is lowercase
        if i in LowAlp:
            textVal = LowAlp.index(i)
            strVal = abs(26 + textVal - keyVal) % 26
            str_decode += LowAlp[strVal]
            if keyIndex == (len(key) - 1):
                keyIndex = 0
            else:
                keyIndex += 1

        # if the letter in the ciphertext is uppercase
        elif i in UpAlp:
            textVal = UpAlp.index(i)
            strVal = abs(26 + textVal - keyVal) % 26
            str_decode += UpAlp[strVal]
            if keyIndex == (len(key) - 1):
                keyIndex = 0
            else:
                keyIndex += 1
        
        # if there is anything but a letter in the ciphertext
        else:
            str_decode += i

    return str_decode

## MAIN ##
# checking if user input allowable flags
if (sys.argv[1] != "-e") & (sys.argv[1] != "-d"):
    print("ERROR: Invalid flag")
    sys.exit()

# check if key is given
try:
    if (sys.argv[2] == "") | (sys.argv[2] == "\n"):
        print("ERROR: Invalid key input")
        sys.exit()

# catch error and display that no key is given
except IndexError:
    print("ERROR: No key given")
    sys.exit()

# the actual start of the program
# declare the flag and the key for encode/decode
flag = sys.argv[1]
key = sys.argv[2]

# loop program
while(1):
    # take input from user
    try:
        text = input('')

    except EOFError:
        sys.exit()

    # encode or decode the text
    if flag == "-e":
        print(Encode(text, key))

    elif flag == "-d":
        print(Decode(text, key))
