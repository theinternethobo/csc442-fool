###############################################
# Timothy Huhn, Aankit Pokhrel, Jerome Reed,
# Jared Andra , Josh Iselin , Ibrahim AL-Agha,
# David Amort, and Brendon Burd
#
# (The Fool - CYEN 301)
# 4/29/2021
# TimeLock
###############################################
import hashlib
import time
from datetime import datetime
import sys

DEBUG = False
DEBUG_TIME = False # use default time over system's current time
TIME = "2017 04 26 15 14 30" # default time to use for debugging

## SUBROUTINES ##
# Calculate time elapsed (seconds) of current system time since epoch time
# Daylight savings needs to be considered!
def Calc_Time_Elapsed(epoch_time, sys_time):
    # get the int values of each date/time value
    epoch = time.strptime(epoch_time, "%Y %m %d %H %M %S")
    sys = time.strptime(sys_time, "%Y %m %d %H %M %S")
    
    # determine time elapsed
    elapsed_time = (int)(time.mktime(sys) - time.mktime(epoch))

    # determine time intervals
    interval_0 = elapsed_time - (elapsed_time % 60) # beginning interval
    interval_1 = elapsed_time + (59 -(elapsed_time % 60)) # ending interval

    # for debug, show the int values of epoch and sys as well as
    # elapsed time with its intervals
    if (DEBUG):
        print("\nEpoch:")
        for i in epoch:
            print(i)

        print("\nSystem:")
        for i in sys:
            print(i)
        
        print("\nTime elapsed = {} seconds".format(elapsed_time))
        print("Beginning interval = {} seconds".format(interval_0))
        print("Ending interval = {} seconds".format(interval_1))
        
    # get the hexadecimal value of the elapsed seconds
    Hash(elapsed_time, interval_0, interval_1)

# compute MD5(MD5(time elapsed))
def Hash(elapsed_time, interval_0, interval_1):
    # convert the int objects into string objects
    elapsed_time = (str)(elapsed_time)
    interval_0 = (str)(interval_0)
    interval_1 = (str)(interval_1)

    # hash MD5(MD5(t))
    str_t = hashlib.md5(((hashlib.md5(elapsed_time.encode())).hexdigest()).encode())
    str_0 = hashlib.md5(((hashlib.md5(interval_0.encode())).hexdigest()).encode())
    str_1 = hashlib.md5(((hashlib.md5(interval_1.encode())).hexdigest()).encode())

    # for debug, check each strings hash
    if (DEBUG):
        print("\nstr_t = {}".format(str_t.hexdigest()))
        print("str_0 = {} (*)".format(str_0.hexdigest()))
        print("str_1 = {}\n".format(str_1.hexdigest()))

    # interval_0 is the hash we want to use
    str_hash = str_0.hexdigest()
    Extract_Con(str_hash)

# Extract and concatenate first two letters ([a-f]) of the hash left-to-right
# followed by the first two single-digit integers ([0-9]) of the hash from right-to-left
def Extract_Con(str_hash):
    # get the length of the hash string
    length = len(str_hash)
    # create an empty string to concatenate to
    Code = ""

    i = 0
    j = length - 1
    try:
        while(len(Code) < 2):   
            if str_hash[i] in {'a','b','c','d','e','f'}:
                Code = Code + str_hash[i]
            i = i + 1

        while(len(Code) < 4):
            if str_hash[j] not in {'a','b','c','d','e','f'}:
                Code = Code + str_hash[j]
            j = j - 1

        Code = Code+str_hash[length-1]

        print(Code)
    except IndexError:
        print("Oops! IndexError")
        sys.exit()


## MAIN ##
# get the epoch time in string form
epoch_time = input() # YYYY MM DD HH mm SS
if (len(epoch_time) < 19):
    print("Error: epoch time given is not of valid format!")
    print("Usage: echo \"YYYY MM DD HH mm SS\" | python3 timelock.py")
    sys.exit()

# get system's current time in string form
if (DEBUG_TIME):
    sys_time = TIME # use default time
else:
    sys_time = datetime.now().strftime("%Y %m %d %H %M %S") # YYYY MM DD HH mm SS

# for debug, print epoch time and system's current time
if (DEBUG):
    print("Epoch = {}".format(epoch_time))
    print("System = {}".format(sys_time))

# calculate time elapsed
Calc_Time_Elapsed(epoch_time, sys_time)