import math

def integerFactorial(num):
    if num == 0:
        return 1

    total = 1
    while num > 1:
        total *= num
        num -= 1

    return total
    
def gamma(z):
    return math.sqrt(math.tau / z) * (((z + 1 / (12 * z + 1 / (10 * z))) / math.e) ** z)
    
def factorial(num):
    if int(num) == num:
        return int(integerFactorial(num))
    else:
        return gamma(num + 1)

value = float(input('Enter a number to factorialize.'))
print(f'{value}! = {factorial(value)}')
