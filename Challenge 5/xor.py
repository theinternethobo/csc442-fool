###############################################
# Timothy Huhn, Aankit Pokhrel, Jerome Reed,
# Jared Andra , Josh Iselin , Ibrahim AL-Agha,
# David Amort, and Brendon Burd
#
# (The Fool - CYEN 301)
# 5/3/2021
# XOR Crypto
###############################################
import sys

KEY = 'key'

# xor function
def xor_it(message, key):
    
    # create a variable to append the xor'ed bytes to
    xor_message = bytearray()
    for m, k in zip(message, key):
        xor_message.append(m ^ k)
    
    return xor_message

## MAIN ##
# get the plaintext or the ciphertext
message = bytearray(sys.stdin.buffer.read())

# get the key by reading the specified key file, then close the file
with open(KEY) as i:
    key = bytearray(i.buffer.read())

# xor the plaintext/ciphertext and key, then output the result
sys.stdout.buffer.write(xor_it(message, key))

# close the buffer
sys.stdout.buffer.close()