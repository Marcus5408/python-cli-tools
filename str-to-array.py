#turn a string into an array
def stringToArray(string):
    array = []
    for i in range(0, len(string)):
        array.append(string[i])
    return array

print(stringToArray("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890`~!@#$%^&*()-_+={}[]|\\:;\"'<>,.?/ "))