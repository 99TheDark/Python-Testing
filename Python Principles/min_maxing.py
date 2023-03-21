def largest_difference(arr):
    min_val = 2e50
    max_val = -2e50
    for item in arr:
        min_val = min(min_val, item)
        max_val = max(max_val, item)
    return max_val - min_val

print(largest_difference([1, 2, 3, 4, 5, 8])) # 7
