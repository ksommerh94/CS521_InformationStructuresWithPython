'''

Karen Sommer

CS 521 Spring 2021

Assignment 4

Problem 24 pages 382-387

'''
# Using only list comprehension (no loops) how would you change a list
# of positive integers such as
# [2,3,4,5] and [9,9,1,9] into their actual numbers 2345  and 9919

l1=[2,3,4,5]
l2=[9,9,1,9]

str_l1=[str(l) for l in l1]
str_l2=[str(l) for l in l2]

print("".join(str_l1))
print("".join(str_l2))
