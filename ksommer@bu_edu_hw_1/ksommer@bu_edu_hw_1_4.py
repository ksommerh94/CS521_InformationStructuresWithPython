'''

Karen Sommer

CS 521 Spring 2021

Assignment 3

Problem 4 and 236

'''

#Given the string S with odd length:
#a) write an expression to printhe middle character
#b) write an expression to print the string up to but not including the middle character
#c) write an expression to print the string from the middle character to the end ( not including the middle character)

print ('Enter a string')
s = (input())

if len(s)%2!=0:
    m=int(((len(s)/2)-0.5))
    print("A) Middle character:", s[m])
    print("B) Start to middle string:", s[0:m])
    print("C) Middle to end string:", s[m+1:])
else:
    print("Enter a valid string")
