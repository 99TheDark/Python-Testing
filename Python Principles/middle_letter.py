def mid(string):
    # Even length means no middle
    if(len(string) % 2 == 0):
        return ""
    else:
        return string[int(len(string) / 2)]
        
print(mid("Howdy"))
print(mid("Even"))
