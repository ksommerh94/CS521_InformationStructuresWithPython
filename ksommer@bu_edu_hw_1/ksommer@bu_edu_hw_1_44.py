'''

Karen Sommer

CS 521 Spring 2021

Assignment 3

Problem 44 and 154

'''
import string
#Write a progtamm that prompts for a sentence and calculates the
#number of uppercases letters,lowercases letters, digits and puctuations
#Output the result and neatly formattednd labeled columns

print ('Enter a sentence')
str = (input())
count_upper=0
count_lower=0
count_digits=0
count_punctuation=0

punctuation_result = string.punctuation

for s in str:
    if s.isupper():
        count_upper+=1
    elif s.islower():
        count_lower+=1
    elif s.isdigit():
        count_digits+=1
    elif s in punctuation_result:
        count_punctuation+=1
print("Number of lowercases letters: ",count_lower)
print("Number of uppercases letters: ",count_upper)
print("Number of digits: ",count_digits)
print("Number of punctiations: ",count_punctuation)
