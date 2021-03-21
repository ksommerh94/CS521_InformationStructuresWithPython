'''

Karen Sommer

CS 521 Spring 2021

Assignment 3

Problem 52 and 154

'''
#Write a program that prompts the user to enter a 3 digit number such that the digits
# are in order, for example 123 or 789.
# The program loops until a correct value is entered
flag_loop=True
while flag_loop:
    print ('Enter a 3 digit number')
    number = (input())
    n_list=[]
    for n in number:
        n_list.append(n)
    sorted_list=sorted(n_list)

    if sorted_list==n_list:
        flag_loop=False
