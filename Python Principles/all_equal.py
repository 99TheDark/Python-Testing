def all_equal(arr):
    if(len(arr) == 0):
        return True
    cur = arr[0]
    for item in arr:
        if not cur == item:
            return False
    return True

print(all_equal([1, 2, 3]))
print(all_equal([1, 1, 1]))
print(all_equal([1, 1, 5]))
