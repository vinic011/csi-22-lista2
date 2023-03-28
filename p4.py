def verify(string1,string2):
    for char in string1:
        if char not in string2:
            return False
    return True

print(verify("abc","thgabo"))