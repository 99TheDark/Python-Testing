def is_anagram(a, b):
    return sorted(list(a)) == sorted(list(b))
    
print(is_anagram("typhoon", "opython"))
