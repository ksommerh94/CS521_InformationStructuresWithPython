'''

Karen Sommer

CS 521 Spring 2021

Assignment 4

Problem 14_c pages 476-479

'''
# Letter count using dictionaties, remember to consider spaces as special character
# c) Write a function that takes as input a string and prints a histogram of letter counts
# A histogram can be done with mathplotlib r using a diffrent enght strings of characters
import matplotlib.pyplot as plt

print ('Enter a string')
str = (input())

my_dict={}

for word in str:
    if word.isalpha():
        if word in my_dict:
            my_dict[word]+=1
        else:
            my_dict[word]=1

plt.bar(my_dict.keys(), my_dict.values())
plt.show()
