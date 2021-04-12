'''

Karen Sommer

CS 521 Spring 2021

Assignment 4

Problem 14_B pages 476-479

'''
# Letter count using dictionaties, remember to consider spaces as special character
# B) Write a function that takes as input a string and return a dictirionary of letter counts

print ('Enter a string')
str = (input())

my_dict={}

for word in str:
    if word.isalpha():
        if word in my_dict:
            my_dict[word]+=1
        else:
            my_dict[word]=1
print(my_dict)
