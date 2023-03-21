def consecutive_zeros(string):
    biggest = 0
    streak = 0
    for digit in string:
        if digit == "0":
            streak += 1 # I hate that there is no ++/-- operator
        else:
            streak = 0
        biggest = max(biggest, streak)
    return biggest

print(consecutive_zeros("1001101000110"))
