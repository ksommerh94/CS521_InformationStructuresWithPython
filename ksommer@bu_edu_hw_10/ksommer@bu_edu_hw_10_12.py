'''

Karen Sommer

CS 521 Spring 2021

Assignment 10

Problem 12 pages 610-613

'''
import random
# Design a logarithm class. field should be the base and number.
# provide addition and subtraction operators - remember to adjust base appropriately.
# hint use base 2 or 10 as a canonical base for operators

class Logarithm:
    def __init__(self,number,base):
        self.number=number
        self.base=base

    def __str__(self):
        return 'Lod %d base %d' %(self.number , self.base)

    def __add__(self,other):
        if self.base==other.base:
            return(Logarithm(self.number*other.number , self.base))
        else:
            print('Error Base should be the same for addition')

    def __sub__(self,other):
        if self.base==other.base:
            return(Logarithm(self.number/other.number , self.base))
        else:
            print('Error Base should be the same for substraction')

l1=Logarithm(3,10)
l2=Logarithm(5,10)
print(l2+l1)
print(l2-l1)
