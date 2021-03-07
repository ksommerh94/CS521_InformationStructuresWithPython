# -*- coding: utf-8 -*-

'''
Karen Sommer

CS 521 Spring 2021

Assignment 6

String slicing problems

BASED ON PROF. PINSKYs CODE MADE IN CLASS
'''

# string implementation Spring 2021 CS 521


text = """Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
"""

x_list = list(text)

def print_file(x, cur, sep="^"):
    print(x[:cur] + sep + x[cur:] + "\n" + "-----")
#-----------------------------------------------------------------------------------------
#                            10 as specified in the document
#-----------------------------------------------------------------------------------------

# move cursor to the left
def cmd_h(x, cur):
    if cur > 0:
        cur = cur -1
    return x, cur

# move to the right
def cmd_l(x, cur):
    if cur < len(x) -1:
        cur = cur + 1
    return x, cur

# move vertically up
def cmd_j(x, cur):
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

#move cursor vertically down one line
def cmd_k(x, cur):
    previous = x.rfind("\n", 0, cur)
    a = x.find("\n", cur)
    if a < len(x)-1 :
        delta = cur - previous
        after=x.find("\n", a+1)
        next_line_length = after - a
        if delta <= next_line_length:
            cur = a+ delta
        else:
            cur = after
    else:
        cur = len(x)-1
    return x, cur

# delete char to the left of the cursos
def cmd_X(x, cur):
    if cur > 0:
        left = x[ : cur-1]
        right = x[cur : ]
        cur = cur - 1
        x = left + right
    return x, cur

# remove from cur to end of line
def cmd_D(x, cur):
        pos = x.find("\n",  cur, len(x))
        if pos >=0 :
            x = x[ : cur] + x[pos : ]
        else:
            x = x[ : cur]
        return x, cur

#delete current line and move cursor to the beginning of next line
def cmd_dd(x, cur):
    previous = x.rfind("\n", 0, cur)
    present = x.find("\n", cur)
    after=x.find("\n", present+1)

    if previous==-1:
        x = x[present+1 : ]
    else:
        x = x[ : previous] + x[present : ]
    if after==-1:
        prev_prev= x.rfind("\n", 0, previous)
        cur=prev_prev+1
    else:
        prev = x.rfind("\n", 0, cur)
        cur=prev+1
    return x,cur

#transpose two adjacent lines : change line 1 with line 2
def cmd_ddp(x, cur):
    before = x.rfind("\n", 0, cur)
    present = x.find("\n", cur)
    after=x.find("\n", present+1)

    if after!=-1:
        if before !=-1:
            x= x[:before+1] + x[present+1:after] + x[before:present] + x[after:]
            cur=0
        else:
            x= x[present+1:after] + '\n'+ x[:present] + x[after:]
            cur=0
    else:
        before_before=x.rfind("\n", 0, before)
        x= x[:before_before+1] + x[before+1:present] + x[before_before :before] + x[present:]
        cur=0
        print('cac')



    return x,cur

# find first occurence of target after cursor
def cmd_n(x, cur, target):
    pos = x.find(target, cur, len(x))
    if pos >= 0:
        cur = pos
    return x, cur

#write your representation as text file and save it
def cmd_wq(x,cur):
    f = open("wq_hw6.txt", "r+")
    f.truncate(0)
    f.write(x[:cur] + '^' + x[cur:])
    f.close()

#-----------------------------------------------------------------------------------------
#                            10 made by my own based on vi editor commands
#-----------------------------------------------------------------------------------------


# delete char to right of cursor
def cmd_x(x, cur):
    if cur < len(x) - 1:
        x =  x[ : cur]  + x[cur+1 : ]
    return x, cur

# Go to end of line
def cmd_DollarSign(x, cur):
        cur = x.find("\n",  cur, len(x))
        return x, cur

# append target after cursor
def cmd_a(x, cur, target):
    x = x[ : cur] + target + x[cur : ]
    return x, cur

# replace character at cursor
def cmd_r(x, cur, new_char):
    if cur < len(x) - 1:
        x = x[ : cur] + new_char + x[cur+1 : ]
    return x, cur

#Change from cursor to end of line
def cmd_C(x, cur):
    present = x.find("\n", cur)
    cur=present
    return x, cur

#Insert text before cursor
def cmd_i(x, cur,text):
    x=x[:cur]+text+x[cur:]
    cur=cur+len(text)
    return x, cur

#Insert text at start of line
def cmd_I(x, cur,text):
    previous = x.rfind("\n", 0, cur)
    if previous!=0:
        x=x[:previous+1]+text+x[previous+1:]
    else:
        x=text+x[previous+1:]
    return x, cur

#Append text at end of line
def cmd_A(x, cur,text):
    a = x.find("\n", cur)
    if a<len(x)-1:
        x=x[:a]+text+x[a:]
    else:
        x=x[:a]+text
    return x, cur

#Move to start of line (zero)
def cmd_0(x, cur):
    previous = x.rfind("\n", 0, cur)
    if previous!=0:
        cur=previous+1
    else:
        cur=0
    return x, cur

#Move to first  line on screen
def cmd_H(x, cur):
    cur=0
    return x, cur


#-----------------------------------------------------------------------------------------
#                                       PRINTS FOR TESTING
#-----------------------------------------------------------------------------------------


cursor = 65

print_file(text, cursor, "^")
print('10 made by my own based on vi editor commands')

print('cmd_x:')
text, cursor =cmd_x(text, cursor)
print_file(text, cursor)

print('cmd_DollarSign:')
text, cursor =cmd_DollarSign(text, cursor)
print_file(text, cursor)

print('cmd_a:')
text, cursor = cmd_a(text, cursor , "nice ")
print_file(text, cursor)

print('cmd_r:')
text, cursor = cmd_r(text, cursor , "N")
print_file(text, cursor)

print('cmd_C:')
text, cursor = cmd_C(text, cursor)
print_file(text, cursor)

print('cmd_i:')
text, cursor =cmd_i(text, cursor,'hello world ')
print_file(text, cursor)

print('cmd_I:')
text, cursor = cmd_I(text, cursor , 'TESTING')
print_file(text, cursor)

print('cmd_A:')
text, cursor = cmd_A(text, cursor,'TEST')
print_file(text, cursor)

print('cmd_0:')
text, cursor = cmd_0(text, cursor)
print_file(text, cursor)

print('cmd_H:')
text, cursor = cmd_H(text, cursor)
print_file(text, cursor)



print('10 as specified in the document')

print('cmd_h:')
text, cursor = cmd_h(text, cursor)
print_file(text, cursor, "^")

print('cmd_l:')
text, cursor = cmd_l(text, cursor)
print_file(text, cursor, "^")

print('cmd_j:')
text, cursor = cmd_j(text, cursor)
print_file(text, cursor)

print('cmd_k:')
text, cursor = cmd_k(text, cursor)
print_file(text, cursor)

print('cmd_X:')
text, cursor = cmd_X(text, cursor)
print_file(text, cursor)

print('cmd_D:')
text, cursor = cmd_D(text, cursor)
print_file(text, cursor)

print('cmd_dd:')
text, cursor = cmd_dd(text, cursor)
print_file(text, cursor)

print('cmd_ddp:')
text, cursor = cmd_ddp(text, cursor)
print_file(text, cursor)

print('cmd_n:')
text, cursor = cmd_n(text, cursor, "complex")
print_file(text, cursor)

print('cmd_wq:')
cmd_wq(text, cursor)
print('Save!')
