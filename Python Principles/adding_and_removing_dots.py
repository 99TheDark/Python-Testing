def add_dots(string):
    result = ""
    for letter in string:
        result += letter + "."
    return result[:-1]
    
def remove_dots(string):
    return string.replace(".", "")
    
print(remove_dots(add_dots("Hi there")))
