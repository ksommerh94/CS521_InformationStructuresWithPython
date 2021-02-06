'''

Karen Sommer

CS 521 Spring 2021

Assignment 2

Problem 28 and 78

'''


#(Integer operators)
#One way to determine whether an integer is even is to divide the number by two and check the remainder.
#Write a three-line program that prompts for a number,
#converts the input to an integer and
#prints a zero (0) if the number is even and a
#one (1) if the number is odd.

print ('Enter a number')
n = int(input())

if n%2 == 0:
    print('0')
else:
    print('1')
