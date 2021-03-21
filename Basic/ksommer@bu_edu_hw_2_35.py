'''

Karen Sommer

CS 521 Spring 2021

Assignment 2

Problem 35 and 78

'''

#Consider a triang_le with sides of length 3, 7, and 9.
#The law of cosines states that given three sides of a triang_le (a, b, and c)
#and the ang_le C between sides a and b: c**2 = a**2 + b**2 − 2*a*b*cos(C ).
#Write Python code to calculate the three ang_les in the triang_le.

import math
a=3
b=7
c=9

ang_A = math.degrees(math.acos((c**2 - b**2 - a**2)/(-2.0 * a * b)))
ang_B = math.degrees(math.acos((a**2 - c**2 - b**2)/(-2.0 * b * c)))
ang_C = math.degrees(math.acos((b**2 - a**2 - c**2)/(-2.0 * c * a)))


check=ang_A+ang_B+ang_C
#check if sum of angles is 180
#print(check)
print(ang_A)
print(ang_B)
print(ang_C)
