def format_number(num):
    rev = str(num)[::-1]
    temp = ""
    for i in range(len(rev)):
        temp += rev[i]
        if i % 3 == 2 and not i == len(rev) - 1:
            temp += ","
    return temp[::-1]

print(format_number(100000))
