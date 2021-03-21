'''

Karen Sommer

CS 521 Spring 2021

Assignment 5

Problem 12 pages 264-267

'''
#A leap year in the Gregorian claendar system is a year that is divisible by 4 but not by 100
# unless it is also divisible by 400. For example 1896, 1904 and 2000 were elap years
# but 1900 was not. Write a function that takes in year as input and prits whether it's a leap year or not

def leap_year(year):
    if (year%4==0) and (year%100!=0 or year%400==0 ):
        print('The year ',year,' is leap year')
    else:
        print('The year ',year,' is not leap year')

if __name__ == "__main__":
    year = int(input("Please enter a Year: "))
    leap_year(year)
