from askUser import *
from random import *

length = askUserInt("Enter length of string: ", "Input must be a positive integer")
repeat = input("Enter number of times to repeat: ")
if repeat == "":
    repeat = True
## generate a random string
randomString = ""
i = 0
while i != repeat:
    for n in range(0, length):
        characters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '`', '~', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '+', '=', '{', '}', '[', ']', '|', '\\', ':', ';', '"', "'", '<', '>', ',', '.', '?', '/']
        randomString += characters[randint(0, len(characters))]
        n += 1
    print("Trying " + str(randomString) + "...")
    i += 1