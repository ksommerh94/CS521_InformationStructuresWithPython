'''

Karen Sommer

CS 521 Spring 2021

Assignment 4

Problem 14_A pages 476-479

'''
# Letter count using dictionaties, remember to consider spaces as special character
# a) Write a function that takes as input a string and return the most common letter in the string

print ('Enter a string')
str = (input())

my_dict={}

for word in str:
    if word.isalpha():
        if word in my_dict:
            my_dict[word]+=1
        else:
            my_dict[word]=1

values = my_dict.values()
best = max(values)
common_words = []
for k in my_dict:
    if my_dict[k] == best:
        common_words.append(k)
print (common_words)
