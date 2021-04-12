'''

Karen Sommer

CS 521 Spring 2021

Assignment 3

Problem 12 and 154

'''
import math

#Write a program that counts numbers of odd numbers, even numbers and squares from 2 to 25 (inclusive)

counter_even=0
counter_odd=0
counter_square=0

for i in range(2,26):
    if math.sqrt(i).is_integer() :
        counter_square+=1
    if i%2==0:
        counter_even+=1
    if i%2!=0:
        counter_odd+=1


print("Even numbers between 2 and 25: ",counter_even)
print("Odd numbers between 2 and 25: ",counter_odd)
print("Square numbers between 2 and 25: ",counter_square)
