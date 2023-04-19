import math

def integral(func, start, stop, increment = 0.0001):
    ran = [val * increment for val in range(start, int(stop / increment))] # Decimal increment
    sum = 0
    for i in ran:
        # increment + i / 2 is better generally for rougher increments
        sum += increment * func(i)
    return sum

def circle(x):
    return math.sqrt(4 - x * x)

print(integral(circle, 0, 2))
