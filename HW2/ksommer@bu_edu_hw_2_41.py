'''

Karen Sommer

CS 521 Spring 2021

Assignment 2

Problem 41 and 78

'''
import math


#An NBA basketball has a diameter of 25 cm.
#Calculate the surface area of the basketball in cm**2.


d=25
r=d/2

sarea=4*math.pi*(r**2)

print('The surface area of the basketball : ',round(sarea,3) , 'cm^2')
