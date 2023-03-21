def flatten(array):
    arr = []
    for sub in array:
        for item in sub:
            arr.append(item)
    return arr
    
print(flatten([[1, 2], [3, 4, 5]]))
