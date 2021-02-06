'''

Karen Sommer

CS 521 Spring 2021

Assignment 2

Problem 10 and 78

'''


#A nursery rhyme: As I was going to St. Ives, I met a man with seven wives.
#Every wife had seven sacks, and every sack had seven cats, every cat had seven kittens.
#Kittens, cats, sacks, and wives, how many were going to St. Ives?
#There are interesting aspects to this puzzle, such as who is actually going to St. Ives.
#For our purposes, assume that everyone and everything are headed to St. Ives.
#Write a program to calculate that total.

#7** (4 (Kittens, cats, sacks, and wives))
total=0
for i in range(5):
    total+=7**i
print(total)
