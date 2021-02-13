'''

Karen Sommer

CS 521 Spring 2021

Assignment 3

Problem 7 and 236

'''

#Given the string variable x = 'acegikmoqsuwy' and y = '+bdfhj lnprtvxz'
#use indexing to create a string z that is the lowercase English alphabet.

x = 'acegikmoqsuwy'
y = '+bdfhj lnprtvxz'
z=''
total=x+y

for t in total:
    if t.isalpha():
        z+=t

print('The lowercase English alphabet is : ',z)
