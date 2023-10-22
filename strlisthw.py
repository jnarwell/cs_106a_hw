#something
def something(s):
    if 'some' in s.lower() or 'thing' in s.lower():
        return True
    else:
        return False

#post_at
def post_at(s):
    n = s.find('@')+1
    fn = len(s)
    
    if fn-n >= 3 and n>0:
        return s[n:fn]
    else:
        return None

#at_swap
def at_swap(s):
    n = s.find('@@@')+3
    fn = len(s)
    
    if n>2:
        return s[n:fn]+s[0:n-3]
    else:
        return ''

#find_plus
def find_plus(s):
    n1 = s.find('+')+1
    n2 = s.find('+', n1)
    
    if n1>0 and n2>-1:
        return s[n1:n2]
    else:
        return ''

#count_up
def count_up(s):
    n = 0
    for x in s:
        if x.isupper():
            n+=1
    return n

#special
def special(s):
    n = s.find('#')
    if len(s)>n+2 and s[n+1].isalpha() and s[n+2].isnumeric():
        return int(s[n+2])*123
    else:
        return -1

#at_sum
def at_sum(s):
    n1 = s.find('@')
    n2 = s.find('@', n1+1)

    if n1>-1 and n2>-1:
        return int(s[n1+1]) + int(s[n2+1])
    else:
        return 0
    
#first_alpha
def first_alpha(s):
    a = -1
    for i in range(len(s)):
        if s[i].isalpha():
            a = i
            break
    return a
        
#char_plus
def char_plus(s):
    new = ''
    for ch in s:
        if ch.isalpha() or ch == '+':
            new+=ch
    return new

#char_misc
def char_misc(s):
    n = ''
    for ch in s:
        if not ch.isalpha() and not ch.isnumeric():
            n+=ch
    return n

#lower_upper
def lower_upper(s):
    n1 = ''
    n2 = ''
    for c in s:
        if c.isalpha():
            if c.isupper():
                n2+=c
            else:
                n1+=c
    return n1+n2

#alpha_list
def alpha_list(s):
    l = []
    for c in s:
        if c.isalpha():
            l.append(c)
    return l

#yolo_index
def yolo_index(strings):
    if 'yolo' in strings:
        return strings.index('yolo')
    else:
        return -1

#food_index
def food_index(foods):
    if 'coffee' in foods:
        return foods.index('coffee')
    elif 'donut' in foods:
        return foods.index('donut')
    else:
        return -1