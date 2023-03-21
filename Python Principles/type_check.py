def only_ints(a, b):
    return type(a) is int and type(b) is int
    
only_ints(1, 2)
only_ints("a", 1)
only_ints(5.3, 7)
