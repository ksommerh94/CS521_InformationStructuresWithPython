'''

Karen Sommer

CS 521 Spring 2021

Assignment 2

Problem 40 A and 78

'''


#Body Mass Index (BMI) is a number calculated from a person’s weight and height.
#According to the Centers for Disease Control, the BMI is a fairly reliable indicator of body fatness for most people.
#BMI does not measure body fat directly,
#but research has shown that BMI correlates to direct measures of body fat,
#such as underwater weighing and dual energy X-ray absorptiometry.
#The formula for BMI is: weight/height**2
#where weight is in kilograms and height is in meters.
#a. Write a program that prompts for metric weight and height and outputs the BMI.


print ('Enter a weight in KG')
w = float(input())
print ('Enter a height in meters')
h = float(input())

BMI= w/h**2
print('BMI: ',round(BMI,2))
