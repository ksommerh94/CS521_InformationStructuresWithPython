'''

Karen Sommer

CS 521 Spring 2021

Assignment 4

Problem 24_B pages 382-387

'''
# Make a list of the words in a sentence. No punctuationhould be attached to  "word" in your list,
# for example, "end." is not corrected word,but "end" is
# Use for loop

import re
print ('Enter a sentence')
str = (input())

list_str=str.split()

for e,i in enumerate(list_str):
    if not i.isalnum():
        list_str[e] = re.sub(r'[^a-zA-Z0-9]', '', i)

print(list_str)
