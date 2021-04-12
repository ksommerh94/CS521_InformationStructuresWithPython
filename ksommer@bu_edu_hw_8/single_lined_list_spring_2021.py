# -*- coding: utf-8 -*-
"""
Created on Wed Mar 17 07:49:57 2021

@author: epinsky
"""

# editor double linked list spring 2021


DATA = 0; NEXT_PTR = 1
x="""the boy
with striped
payjama"""
x_list = x.split('\n')

def get_list(y):
    head = None; tail = None
    for e in y:
        node = [e, None]
        if head is None:
            head = node
            tail = node
        else:
            tail[NEXT_PTR] = node
            tail = node
    return head, tail

def print_list(head, tail):
    node = head
    while node is not None:
        print(node[DATA])
        node = node[NEXT_PTR]
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
    
h, t = get_list(x_list)
# print_list(h, t)
z = get_node(h, t, 1)
print(z[DATA])

    