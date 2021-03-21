'''

Karen Sommer

CS 521 Spring 2021

Assignment 3

Problem 47 and 154

'''
import string
#You are creating a new account and need to provide a password.
#The password has the following requiremnts
#a) The password must be at least 6 characters and most 20 charcaters
#b)It must contain atc least one lowercase letter, one uppercase letter
#     and one Number
#write a program that propts the user to input a password and checks if the password
#is valid. If the password is valid, print a confirmation stament.
#If not print a no valid statemnt

print ('Enter a password')
pwd = (input())

flag_uppercase=False
flag_lowercase=False
flag_number=False

if (len(pwd)>6 and len(pwd)<21):
    for p in pwd:
        if p.isdigit():
            flag_number=True
        elif p.islower():
            flag_lowercase=True
        elif p.isupper():
            flag_uppercase=True

    if flag_uppercase==False or flag_lowercase==False or flag_number==False:
        print('Invalid password')
    else:
        print('All set!')


else:
    print('Not valid lenght password')
