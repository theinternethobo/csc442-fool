from pynput.keyboard import Key, Controller
from time import sleep
from random import randint
from termios import tcflush, TCIFLUSH
from sys import stdin, stdout

DEBUG = False

password = input()
features = input()

# split the password
password = password.split(",")
password = password[:len(password)//2+1]
# join the chars into a single string
password = "".join(password)

# split the features
features = features.split(",")
features = [float(a) for a in features]

if (DEBUG):
    print("password = {}".format(password))
    print("features = {}".format(features))

# how long (seconds) the key has been pressed for???
keypress = features[:len(features)//2+1]
# how long (seconds) till the next key is pressed???
keyinterval = features[len(features)//2+1:]

if (DEBUG):
    print("keypress = {}".format(keypress))
    print("keyinterval = {}".format(keyinterval))

keyboard = Controller()
i = 0

sleep(5)

for char in password:
    keyboard.press(char)
    sleep(keypress[i])
    keyboard.release(char)
    if (i < len(keyinterval)):
        sleep(keyinterval[i])
        i = i + 1

keyboard.press(Key.enter)
keyboard.release(Key.enter)

tcflush(stdout, TCIFLUSH)
print()