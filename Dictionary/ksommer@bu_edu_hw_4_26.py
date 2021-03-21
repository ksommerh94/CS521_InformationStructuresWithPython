'''

Karen Sommer

CS 521 Spring 2021

Assignment 4

Problem 26 pages 476-479

'''
# Use a dictionary to cerate a program that prompts for an integer and prints out the integer using words.
# For example 138 will print "one three eight"

num_dict={1:'one',2:'two',3:'three',4:'four',5:'five',6:'six',7:'seven',8:'eight',9:'nine',0:'zero'}

print ('Enter a number')
number = (input())
name_number=[]

for n in number:
    name_number.append(num_dict[int(n)])

print(' '.join(name_number))
