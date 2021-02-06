'''

Karen Sommer

CS 521 Spring 2021

Assignment 2

Problem 40B and 78

'''



#Body Mass Index (BMI) is a number calculated from a person’s weight and height.
#According to the Centers for Disease Control, the BMI is a fairly reliable indicator of body fatness for most people.
#BMI does not measure body fat directly,
#but research has shown that BMI correlates to direct measures of body fat,
#such as underwater weighing and dual energy X-ray absorptiometry.
#The formula for BMI is: weight/height**2
#where weight is in kilograms and height is in meters.
#b. Write a program that prompts for weight in pounds and height in inches, converts the values to metric, and then calculates the BMI.


print ('Enter a weight in pounds')
wpd = float(input())
print ('Enter a height in inches')
hi = float(input())

wkg=wpd*0.45359237
hmts=hi*0.0254

BMI= wkg/hmts**2
print('BMI: ',round(BMI,2))
