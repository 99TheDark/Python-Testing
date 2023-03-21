def capital_indexes(string):
    arr = [letter for letter in string]
    indices = []
    for i in range(len(arr)):
        if(arr[i].isupper()):
            indices.append(i)
    return indices
    
print(capital_indexes("HeLlO tHerE"))
