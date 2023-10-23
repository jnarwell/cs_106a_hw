#first_alpha
def first_alpha(s):
    i = 0
    while i < len(s):
        if s[i].isalpha():
            return i
        i+=1
    return -1
        
