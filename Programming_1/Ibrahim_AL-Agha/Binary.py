#!/usr/bin/env python3

import sys

data = sys.stdin.readline()

def foo(str_input):
    return (''.join(chr(int(data[i*8:i*8+8],2)) for i in range(len(data)//8)))

print(foo(data))
