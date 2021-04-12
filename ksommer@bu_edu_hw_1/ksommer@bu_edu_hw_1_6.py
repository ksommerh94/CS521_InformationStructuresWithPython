'''

Karen Sommer

CS 521 Spring 2021

Assignment 3

Problem 6 and 151

'''


#Write a "for" loop that will print "pbil"when "alphabetical" is the input

str="alphabetical"

for e,i in enumerate(str):
    if (i=="p" or i=="b" or i=="i" or i=="l") and e >1:
        print(i)
