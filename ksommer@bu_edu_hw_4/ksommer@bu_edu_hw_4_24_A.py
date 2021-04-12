'''

Karen Sommer

CS 521 Spring 2021

Assignment 4

Problem 24_A pages 382-387

'''
# Make a list of the words in a sentence. No punctuationhould be attached to  "word" in your list,
# for example, "end." is not corrected word,but "end" is
# A) Use while loop
import re
print ('Enter a sentence')
str = (input())

list_str=str.split()

i=0
while i<  len(list_str):
    if not list_str[i].isalnum():
        list_str[i] = re.sub(r'[^a-zA-Z0-9]', '', list_str[i])
    i+=1

print(list_str)
