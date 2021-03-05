# -*- coding: utf-8 -*-
"""
Created on Wed Mar  3 08:54:01 2021

@author: epinsky
"""

# string implementation Spring 2021 CS 521


text = """Angels and
demons is book
about illuminari 
today"""

cursor = 4
x_list = list(text)

def print_file(x, cur, sep="$"):
    print(x[:cur] + sep + x[cur:] + "\n" + "-----")
    
def cmd_h(x, cur):   # move cursor to the left 
    if cur > 0:
        cur = cur -1
    return x, cur
    
def cmd_I(x, cur):     # move to the right
    if cur < len(x) -1:
        cur = cur + 1
    return x, cur

def cmd_X(x, cur): # delete char to the left of the cursos
    if cur > 0:
        left = x[ : cur-1]
        right = x[cur : ]
        cur = cur - 1
        x = left + right
    return x, cur


def cmd_x(x, cur):   # delete char to right of cursor
    if cur < len(x) - 1:
        x =  x[ : cur]  + x[cur+1 : ]
    return x, cur


def cmd_n(x, cur, target):    # find first occurence of target after cursor
    pos = x.find(target, cur, len(x))
    if pos >= 0:
        cur = pos
    return x, cur


def cmd_a(x, cur, target): # append target after cursor
    x = x[ : cur] + target + x[cur : ]
    return x, cur
    
def cmd_r(x, cur, new_char):    # replace character at cursor
    if cur < len(x) - 1:
        x = x[ : cur] + new_char + x[cur+1 : ]
    return x, cur
        
        
def cmd_D(x, cur):  # remove from cur to end of line
        pos = x.find("\n",  cur, len(x))
        if pos >=0 :
            x = x[ : cur] + x[pos : ]
        else:
            x = x[ : cur]
        return x, cur
    
def cmd_j(x, cur):     # move vertically up  
    a = x.rfind("\n", 0, cur)
    if a >0 :
        delta = cur - a
        b = x.rfind("\n", 0, a-1)
        prev_line_length = a - b
        if delta <= prev_line_length:
            cur = b + delta
        else:
            cur = a - 1
    return x, cur
        
        
    
    

"""
print_file(text, cursor, "$")
text, cursor = cmd_I(text, cursor)
print_file(text, cursor, "$")
   
print_file(text, cursor, "$")
text, cursor = cmd_h(text, cursor)
print_file(text, cursor, "$")
cursor = 0
print_file(text, cursor, "$")
text, cursor = cmd_h(text, cursor)
print_file(text, cursor, "$")


cursor = 0
print_file(text, cursor, "$")
text, cursor = cmd_X(text, cursor)
print_file(text, cursor, "$")
"""
"""
cursor = 4
print_file(text, cursor, "$")
text, cursor = cmd_n(text, cursor, "book")
print_file(text, cursor, "$")

text, cursor = cmd_n(text, cursor, "Vatican")
print_file(text, cursor, "$")
"""

cursor = 4
print_file(text, cursor, "$")
text, cursor = cmd_n(text, cursor, "book")
print_file(text, cursor, "$")

text, cursor = cmd_a(text, cursor , "nice ")
print_file(text, cursor, "$")


text, cursor = cmd_r(text, cursor , "N")
print_file(text, cursor, "$")

text, cursor = cmd_x(text, cursor )
print_file(text, cursor, "$")

text, cursor = cmd_D(text, cursor)
print_file(text, cursor, "$")


cursor = 43
print_file(text, cursor, "$")
text, cursor = cmd_D(text, cursor)
print_file(text, cursor, "$")

cursor = 35
print_file(text, cursor, "$")
text, cursor = cmd_j(text, cursor)
print_file(text, cursor)







