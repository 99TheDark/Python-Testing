def validate(code):
    if not "def" in code:
        return "missing def"
    if not ":" in code:
        return "missing :"
    if not ("(" in code and ")" in code):
        return "missing paren"
    if "()" in code.split("\n")[0]:
        return "missing param"
    if not "    " in code:
        return "missing indent"
    if not "validate" in code:
        return "wrong name"
    if not "return" in code:
        return "missing return"
    return True
    
print(validate("""
def validate(code):
    if not "def" in code:
        return "missing def"
    if not ":" in code:
        return "missing :"
    if not ("(" in code and ")" in code):
        return "missing paren"
    if "()" in code.split("\n")[0]:
        return "missing param"
    if not "    " in code:
        return "missing indent"
    if not "validate" in code:
        return "wrong name"
    if not "return" in code:
        return "missing return"
    return True
"""))
