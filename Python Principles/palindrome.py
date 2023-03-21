def palindrome(string):
    return string[::-1] == string
    
print(palindrome("bob"))
print(palindrome("abba"))
print(palindrome("abcd"))
