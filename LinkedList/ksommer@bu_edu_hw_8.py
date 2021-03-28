# -*- coding: utf-8 -*-
'''
Karen Sommer

CS 521 Spring 2021

Assignment 8

Linked List problems

BASED ON PROF. PINSKYs CODE MADE IN CLASS
'''

DATA = 0; NEXT_PTR = 1; PREV_PTR = 2

x = """Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated."""

x_list = x.split('\n')

def get_list(y):
    head = None; tail = None
    for e in y:
        node = [e, None, None]
        if head is None:
            head = node
            tail = node
        else:
            tail[NEXT_PTR] = node
            node[PREV_PTR] = tail
            tail = node
    return head, tail

def print_list(head, tail):
    node = head
    while node is not None:
        print(node[DATA])
        node = node[NEXT_PTR]
    return

def print_file(head, tail, my_node, delta, sep="^"):
    node = head
    while node is not None:
        if node is not my_node:
            print(node[DATA])
            node = node[NEXT_PTR]
        else:
            my_data = my_node[DATA]
            print(my_data[:delta] + sep + my_data[delta:])
            node =  node[NEXT_PTR]
    print("---------------")
    return

def get_node(head, tail, pos):
    node = head
    counter = 0
    while node is not None:
        if counter == pos:
            return node
        elif counter > pos:
            return tail
        else:
            node = node[NEXT_PTR]
            counter = counter + 1

#-----------------------------------------------------------------------------------------
#                            10 as specified in the document
#-----------------------------------------------------------------------------------------

def cmd_h(head, tail, my_node, pos):  # move left one position
    if pos > 0:
        pos = pos -1
    else:
        if my_node[PREV_PTR] is not None:
            my_node = my_node[PREV_PTR]
            my_data = my_node[DATA]
            pos = len(my_data)+1
    return head, tail, my_node, pos

def cmd_l(head, tail, my_node, pos):  # move right one position
    my_data = my_node[DATA]
    if pos < len(my_data):
        pos = pos + 1
    else:
        if my_node[NEXT_PTR] is not None:
            my_node = my_node[NEXT_PTR]
            pos = 0
    return head, tail, my_node, pos

def cmd_j(head, tail, my_node, pos):  # move up vertically one line
    if my_node != head:
        prev_node=my_node[PREV_PTR]
        prev_data=prev_node[DATA]
        if pos <= len(prev_data):
            my_node=my_node[PREV_PTR]
        else:
            my_node=my_node[PREV_PTR]
            pos=len(prev_data)
    return head, tail, my_node, pos

def cmd_k(head, tail, my_node, pos):    # move down vertically one line
    if my_node != tail:
        nxt_node=my_node[NEXT_PTR]
        nxt_data=nxt_node[DATA]
        if pos <= len(nxt_data):
            my_node=my_node[NEXT_PTR]
        else:
            my_node=my_node[NEXT_PTR]
            pos=len(nxt_data)
    return head, tail, my_node, pos

def cmd_X(head, tail, my_node, pos):   # delete one char to left
    if pos > 0:
        my_data = my_node[DATA]
        new_data = my_data[:pos-1] + my_data[pos :]
        my_node[DATA] = new_data
        pos = pos - 1
    return head, tail, my_node, pos

def cmd_D(head, tail, my_node, pos): # remove from cursor to end of current line
    if pos==0:
        if my_node==tail:
            my_node[PREV_PTR][NEXT_PTR]=None
        else:
            prev_node=my_node[PREV_PTR]
            nxt_node=my_node[NEXT_PTR]
            prev_node[NEXT_PTR]=my_node[NEXT_PTR]
            nxt_node[PREV_PTR]=my_node[PREV_PTR]
            my_node=prev_node
    else:
        data=my_node[DATA]
        my_node[DATA] = data[ : pos]

    return head, tail, my_node, pos

def cmd_dd(head, tail, my_node, pos):  # delete current line, move to start of next line, only if have next line
    if my_node!= tail:
        prev_node=my_node[PREV_PTR]
        nxt_node=my_node[NEXT_PTR]
        prev_node[NEXT_PTR]=my_node[NEXT_PTR]
        nxt_node[PREV_PTR]=my_node[PREV_PTR]
        my_node=nxt_node
        pos=0

    return head, tail, my_node, pos

def cmd_ddp(head, tail, my_node, pos): # transpose two adjacent line
    if my_node!= tail:
        nxt_node=my_node[NEXT_PTR]
        my_node,nxt_node=nxt_node,my_node
        if pos>len(my_node[DATA]):
            pos=len(my_node[DATA])
    return head, tail, my_node, pos

def cmd_n(head, tail, my_node, pos, target): # find first occurence of target after cursor
    next_node = my_node
    while next_node is not None:
        my_data = next_node[DATA]
        my_pos = my_data.find(target)
        if my_pos >= 0:
            return head, tail, next_node, my_pos
        next_node = next_node[NEXT_PTR]
    return head, tail, my_node, pos

def cmd_wq(head, file_name): #write your representation as text file and save it
    f = open(file_name, "a")
    f.truncate(0)
    str=''
    node = head
    while node is not None:
        str=(node[DATA])
        str+="\n"
        node = node[NEXT_PTR]
        f.writelines(str)
    f.close()
    print('Saved!')

#-----------------------------------------------------------------------------------------
#                            10 made by my own
#-----------------------------------------------------------------------------------------

def cmd_x(head, tail, my_node, pos): # delete character to right
    my_data=my_node[DATA]
    if pos<len(my_data):
        my_node[DATA]= my_data[: pos] + my_data[ pos+1 : ]
    return head, tail, my_node, pos

def cmd_DollarSign(head, tail, my_node, pos): # Go to end of line
    pos=len(my_node[DATA])
    return head, tail, my_node, pos

def cmd_a(head, tail, my_node, pos,target): # append target after cursor
    my_data=my_node[DATA]
    my_node[DATA]=my_data[:pos] + target + my_data[pos : ]
    return head, tail, my_node, pos

def cmd_r(head, tail, my_node, pos,target): # replace character at cursor
    my_data=my_node[DATA]
    my_node[DATA]=my_data[:pos] + target + my_data[pos+1 : ]
    return head, tail, my_node, pos

def cmd_C(head, tail, my_node, pos,change):#Change rest of line
    my_data=my_node[DATA]
    my_node[DATA]=my_data[:pos] + change
    return head, tail, my_node, pos

def cmd_i(head, tail, my_node, pos,target):# append target before cursor
    my_data=my_node[DATA]
    my_node[DATA]=my_data[:pos] + target + my_data[pos : ]
    pos+= len(target)
    return head, tail, my_node, pos

def cmd_I(head, tail, my_node, pos,target):# Insert text at start of line
    my_data=my_node[DATA]
    my_node[DATA]=target + my_data
    pos+= len(target)
    return head, tail, my_node, pos

def cmd_A(head, tail, my_node, pos,target):# Insert text at start of line
    my_data=my_node[DATA]
    my_node[DATA]= my_data + target
    return head, tail, my_node, pos

def cmd_0(head, tail, my_node, pos): #Move to start of line (zero)
    pos=0
    return head, tail, my_node, pos

def cmd_H(head, tail, my_node, pos): #Move to first  line on screen
    my_node=head
    pos=0
    return head, tail, my_node, pos

h, t = get_list(x_list)
# print_list(h, t)
my_node = get_node(h, t, 1)
delta = 22
print_file(h, t, my_node, delta)



#-----------------------------------------------------------------------------------------
#                                       PRINTS FOR TESTING
#-----------------------------------------------------------------------------------------


print('10 as specified in the document')

print('cmd_h:')
h, t, my_node, delta = cmd_h(h, t, my_node, delta)
print_file(h, t, my_node, delta)

print('cmd_l:')
h, t, my_node, delta = cmd_l(h, t, my_node, delta)
print_file(h, t, my_node, delta)

print('cmd_j:')
h, t, my_node, delta = cmd_j(h, t, my_node, delta)
print_file(h, t, my_node, delta)

print('cmd_k:')
h, t, my_node, delta = cmd_k(h, t, my_node, delta)
print_file(h, t, my_node, delta)

print('cmd_X:')
h, t, my_node, delta = cmd_X(h, t, my_node, delta)
print_file(h, t, my_node, delta)

print('cmd_D:')
h, t, my_node, delta = cmd_D(h, t, my_node, delta)
print_file(h, t, my_node, delta)

print('cmd_dd:')
h, t, my_node, delta = cmd_dd(h, t, my_node, delta)
print_file(h, t, my_node, delta)

print('cmd_ddp:')
h, t, my_node, delta = cmd_ddp(h, t, my_node, delta)
print_file(h, t, my_node, delta)

h,t, my_node, delta = cmd_n(h,t, my_node, delta, "bet")
print_file(h, t, my_node, delta)

print('cmd_wq:')
cmd_wq(h,'wq_hw8.txt')

print('10 made by my own')

print('cmd_x:')
h, t, my_node, delta = cmd_x(h, t, my_node, delta)
print_file(h, t, my_node, delta)

print('cmd_DollarSign:')
h, t, my_node, delta = cmd_DollarSign(h, t, my_node, delta)
print_file(h, t, my_node, delta)

print('cmd_a:')
h,t, my_node, delta =cmd_a(h,t, my_node, delta,'A_CMD')
print_file(h, t, my_node, delta)

print('cmd_r:')
h,t, my_node, delta =cmd_r(h,t, my_node, delta,'R')
print_file(h, t, my_node, delta)

print('cmd_C:')
h,t, my_node, delta =cmd_C(h,t, my_node, delta,'CHANGE')
print_file(h, t, my_node, delta)

print('cmd_i:')
h,t, my_node, delta =cmd_i(h,t, my_node, delta,'ADD')
print_file(h, t, my_node, delta)

print('cmd_I:')
h,t, my_node, delta =cmd_I(h,t, my_node, delta,'START ')
print_file(h, t, my_node, delta)

print('cmd_A:')
h,t, my_node, delta =cmd_A(h,t, my_node, delta,'END ')
print_file(h, t, my_node, delta)

print('cmd_0:')
h,t, my_node, delta =cmd_0(h,t, my_node, delta)
print_file(h, t, my_node, delta)

print('cmd_H:')
h,t, my_node, delta =cmd_H(h,t, my_node, delta)
print_file(h, t, my_node, delta)










'''

h,t, my_node, delta =cmd_H(h,t, my_node, delta)
print_file(h, t, my_node, delta)



h,t, my_node, delta =cmd_0(h,t, my_node, delta)
print_file(h, t, my_node, delta)

h,t, my_node, delta =cmd_A(h,t, my_node, delta,'FINAL ')
print_file(h, t, my_node, delta)

h,t, my_node, delta =cmd_I(h,t, my_node, delta,'START ')
print_file(h, t, my_node, delta)

h,t, my_node, delta =cmd_i(h,t, my_node, delta,'ADD')
print_file(h, t, my_node, delta)

h,t, my_node, delta =cmd_C(h,t, my_node, delta,'CHANGE')
print_file(h, t, my_node, delta)

h,t, my_node, delta =cmd_r(h,t, my_node, delta,'R')
print_file(h, t, my_node, delta)

h,t, my_node, delta =cmd_a(h,t, my_node, delta,'A_CMD')
print_file(h, t, my_node, delta)

h,t, my_node, delta =cmd_DollarSign(h,t, my_node, delta)
print_file(h, t, my_node, delta)

h,t, my_node, delta =cmd_x(h,t, my_node, delta)
print_file(h, t, my_node, delta)

cmd_wq(h,'wq_hw8.txt')

h,t, my_node, delta = cmd_ddp(h,t, my_node, delta)
print_file(h, t, my_node, delta)


h,t, my_node, delta = cmd_dd(h,t, my_node, delta)
print_file(h, t, my_node, delta)

h,t, my_node, delta = cmd_D(h,t, my_node, delta)
print_file(h, t, my_node, delta)

h,t, my_node, delta = cmd_j(h,t, my_node, delta)
print_file(h, t, my_node, delta)

h, t, my_node, delta = cmd_h(h, t, my_node, delta)
print_file(h, t, my_node, delta)
delta = 0
print_file(h, t, my_node, delta)

h, t, my_node, delta = cmd_h(h, t, my_node, delta)
print_file(h, t, my_node, delta)

h, t, my_node, delta = cmd_i(h, t, my_node, delta)
print_file(h, t, my_node, delta)
delta = 12
print_file(h, t, my_node, delta)

h, t, my_node, delta = cmd_i(h, t, my_node, delta)
print_file(h, t, my_node, delta)


h,t, my_node, delta = cmd_n(h,t, my_node, delta, "jam")
print_file(h, t, my_node, delta)


h,t, my_node, delta = cmd_x(h,t, my_node, delta)
print_file(h, t, my_node, delta)

h,t, my_node, delta = cmd_x(h,t, my_node, delta)
print_file(h, t, my_node, delta)

h,t, my_node, delta = cmd_x(h,t, my_node, delta)
print_file(h, t, my_node, delta)
'''
