def double_letters(string):
    last = ""
    for letter in string:
        if(last == letter):
            return True
        last = letter
    return False
  
print(double_letters("hello there!"))
print(double_letters("nono"))
