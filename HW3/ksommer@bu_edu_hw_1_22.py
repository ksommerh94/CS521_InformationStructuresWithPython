'''

Karen Sommer

CS 521 Spring 2021

Assignment 3

Problem 22 and 154

'''
import math

#Write a program that checks to see if a number N is prime.
#A simple approach checks all numbers from 2 un to N, but after some point numbers are checked that need not to be checked.
#For example, numbers grater than root(N) need not be checked.
#Write a program that checks for primality and avoids those unnecessary checks. Remember to import the math module.

print ('Enter a number')
n = int(input())
flag=True
if (n > 1):
    for i in range(2, n):
        if (n % i == 0):
            #print(n,'is not a prime number')
            flag=False

    if flag:
        print(n,' is a prime number')
    else:
        print(n,'is not a prime number')
else:
    print('Enter a valid number')
