'''

Karen Sommer

CS 521 Spring 2021

Assignment 4

Problem 39_A pages 382-387

'''
# Given a list of integers L, use list comprehension to
# A) Find the sum of the even integers in the list L

list_l=[1,3,5,7,2,9,10]

sum_val=[l for l in list_l if l%2==0]
print(sum(sum_val))
