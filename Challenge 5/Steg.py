###############################################
# Timothy Huhn, Aankit Pokhrel, Jerome Reed,
# Jared Andra , Josh Iselin , Ibrahim AL-Agha,
# David Amort, and Brendon Burd
#
# (The Fool - CYEN 301)
# 5/6/2021
# Steg
###############################################
import sys
import math
import argparse

# default values for offset and interval
OFFSET = 0
INTERVAL = 1

# sentinel: {0x00, 0xff, 0x00, 0x00, 0xff, 0x00}
sentinel = [0x00, 0xff, 0x00, 0x00, 0xff, 0x00]

## COMMANDLINE PARSING ##
# source: https://docs.python.org/3/library/argparse.html
parser = argparse.ArgumentParser(conflict_handler='resolve')

# store/retrieve commandline argument (args_SR)
args_SR = parser.add_mutually_exclusive_group(required=True)
args_SR.add_argument('-s', action='store_true')
args_SR.add_argument('-r', action='store_true')

# bit/byte commandline argument (args_bB)
args_bB = parser.add_mutually_exclusive_group(required=True)
args_bB.add_argument('-b', action='store_true')
args_bB.add_argument('-B', action='store_true')

# offset, interval, wrapper, and hidden values commandline arguments
parser.add_argument('-o', default=OFFSET, type=int, required=True, dest='offset')
parser.add_argument('-i', default=INTERVAL, type=int, dest='interval')
parser.add_argument('-w', required=True, dest='wrapper_val')
parser.add_argument('-h', dest='hidden_val')

# parse the arguments and assign them to their respective variables
args = parser.parse_args()

store = args.s
retrieve = args.r
bit = args.b
byte = args.B
offset = args.offset
interval = args.interval
wrapper_val = args.wrapper_val
hidden_val = args.hidden_val
#########################

## SUBROUTINES ##
# byte method storage
def byte_storage(offset, interval, wrapper_file, hidden_file, sentinel):

    # add the hidden file bytes to the wrapper file using the given offset and interval
    i = 0
    while i < len(hidden_file):
        wrapper_file[offset] = hidden_file[i]
        offset += interval
        i += 1

    # append the sentinel bytes to the wrapper file to indicate the end of the hidden file
    i = 0
    while i < len(sentinel):
        wrapper_file[offset] = int(format(ord(chr(sentinel[i])), '08b'), 2)
        offset += interval
        i += 1

    return wrapper_file
    
# byte method extraction
def byte_extraction(offset, interval, wrapper_file, sentinel):

    # create an empty hidden file byte array
    hidden_file = bytearray()

    # while the last 6 bytes of the hidden is not the whole sentinel byte array
    while((hidden_file[-6:] != sentinel) and (offset < len(wrapper_file))):
        hidden_file.append(wrapper_file[offset])
        offset += interval

    return hidden_file

# bit method storage
def bit_storage(offset, interval, wrapper_file, hidden_file, sentinel):

    # append the sentinel bytes to the end of the hiddenfile
    for s in sentinel:
        hidden_file.append(int(format(ord(chr(s)), '08b'), 2))

    # store the bytes from the hidden file into the wrapper file one bit at a time
    i = 0
    while ((i < len(hidden_file) and (offset < len(wrapper_file)))):
        for j in range(0, 8):
            if offset >= len(wrapper_file):
                break
            wrapper_file[offset] &= 0b11111110
            wrapper_file[offset] |= ((hidden_file[i] & 0b10000000) >> 7)
            hidden_file[i] = (hidden_file[i] & 0b01111111) << 1
            offset += interval
        i += 1    

    return wrapper_file

    return

# bit method extraction
def bit_extraction(offset, interval, wrapper_file, sentinel):

    # create an empty hidden file byte array
    hidden_file = bytearray()

    # while the last 6 bytes of the hidden is not the whole sentinel byte array
    while((hidden_file[-6:] != sentinel) and (offset < len(wrapper_file))):
        b = 0

        for j in range(0, 8):
            if offset >= len(wrapper_file):
                break
            b = (b & 0b01111111) << 1
            b += (wrapper_file[offset] & 0b00000001)
            offset += interval

        hidden_file.append(b)

    return hidden_file

#################

## MAIN ##
# open the wrapper file
try:
    with open(wrapper_val) as i:
        wrapper_file = bytearray(i.buffer.read())
except FileNotFoundError:
    print("Wrapper file not found\n")
    sys.exit()

# if bit method
if bit:

    # bit storage
    if store:

        # open hidden file
        try:
            with open(hidden_val) as i:
                hidden_file = bytearray(i.buffer.read())
        except FileNotFoundError:
            print("Hidden file not found\n")
            sys.exit()
        except TypeError:
            print("Hidden file not given when trying to store in wrapper file\n")
            sys.exit()

        output = bit_storage(offset, interval, wrapper_file, hidden_file, sentinel)
    
    # bit extraction
    if retrieve:
        output = bit_extraction(offset, interval, wrapper_file, sentinel)

# if byte method
elif byte:

    # byte storage
    if store:

        # open hidden file
        try:
            with open(hidden_val) as i:
                output = hidden_file = bytearray(i.buffer.read())
        except FileNotFoundError:
            print("Hidden file not found\n")
            sys.exit()
        except TypeError:
            print("Hidden file not given when trying to store in wrapper file\n")
            sys.exit()

        output = byte_storage(offset, interval, wrapper_file, hidden_file, sentinel)
    
    # byte extraction
    if retrieve:
        output = byte_extraction(offset, interval, wrapper_file, sentinel)

# output to stdout
sys.stdout.buffer.write(output)
##########