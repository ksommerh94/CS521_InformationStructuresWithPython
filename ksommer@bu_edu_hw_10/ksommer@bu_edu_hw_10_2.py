'''

Karen Sommer

CS 521 Spring 2021

Assignment 10

Problem 2 pages 610-613

'''
# Augmentthe Rational number class to include multiplication and division.
# Include the ability to accomodate operands if type int
#from __future__ import division

class Rational(object):
    def __init__(self,numerador,denominador = 1):
        self.numerador = numerador
        self.denominador = denominador

    def __str__ (self):
        value=self.numerador/self.denominador
        return str(round(value,2)) + " = Rational number numerator %d and denominator %d" %(self.numerador,self.denominador)

    def __mul__ (self, other):
        return Rational(self.numerador * other.numerador, self.denominador * other.denominador)

    def __truediv__ (self, other):
        return Rational(self.numerador * other.denominador, self.denominador * other.numerador)

r1=Rational(2,3)
r2=Rational(5,6)

print(r1*r2)
print(r1/r2)
