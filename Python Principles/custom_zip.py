def zap(a, b):
    if(len(a) == len(b)):
        arr = []
        for i in range(len(a)): # len(a) and len(b) both work
            arr.append((a[i], b[i]))
        return arr
            
print(zap(
    [0, 1, 2, 3, 4],
    [5, 6, 7, 8, 9]
))
