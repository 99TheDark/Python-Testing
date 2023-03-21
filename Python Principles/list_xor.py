def list_xor(n, list1, list2):
    in_list_1 = not n in list1
    in_list_2 = not n in list2
    if (in_list_1 and in_list_2) or not (in_list_1 or in_list_2):
        return False
    return True
    
print(list_xor(1, [1, 2, 3], [4, 5, 6]))
print(list_xor(1, [0, 2, 3], [1, 5, 6]))
print(list_xor(1, [1, 2, 3], [1, 5, 6]))
print(list_xor(1, [0, 0, 0], [4, 5, 6]))
