import math

def binary(num):
    string = ""
    for i in reversed(range(int(math.log2(num)) + 1)):
        string += str((num >> i) % 2)
    return string
    
def printBinary(num):
    print(f'{num} in binary is {binary(num)}')
    
printBinary(346578)
