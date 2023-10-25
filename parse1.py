#first_alpha
def first_alpha(s):
    i = 0
    while i < len(s):
        if s[i].isalpha():
            return i
        i+=1
    return -1
        
#at_word
def at_word(s):
    a = s.find('@')+1
    n = ''
    if a != 0:
        while a < len(s):
            if not s[a].isalpha():
                break
            n+=s[a]
            a+=1
    return n


#one_is_best
def one_is_best(s):
    o = s.find('1')
    n = ''
    if o != -1:
        while o<len(s):
            if not s[o].isnumeric():
                break
            n+=s[o]
            o+=1
    return n

#exclamation
def exclamation(s):
    s = s[::-1]
    e = s.find('!')
    n = ''
    if e != -1:
        while e<len(s):
            n+=s[e]
            e+=1
            if e<len(s) and not s[e].isalpha():
                break
    return n[::-1]