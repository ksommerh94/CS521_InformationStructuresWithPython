'''

Karen Sommer

CS 521 Spring 2021

Assignment 4

Problem 6 pages 476-479

'''
# If you had 2 lists , one of  first names and one of last names ['Jane','John','Jack'] and ['Doe','Deer','Black']
# Use zip to create a dictionary witht he keys as the first names and values as last names.

first_names=['Jane','John','Jack']
last_names=['Doe','Deer','Black']

final_dictionary = dict(zip(first_names, last_names))
print(final_dictionary)
