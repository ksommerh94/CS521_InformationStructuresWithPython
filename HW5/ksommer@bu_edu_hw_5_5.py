'''

Karen Sommer

CS 521 Spring 2021

Assignment 5

Problem 5 pages 416

'''
# A formula exists for calculation the amount of money in a saving account that begins
# with an initial value (the initial princiapl P) and earns interests with annual interest rate i for n years: P(1+i)
# Write a recursive function that calculates that same value , and check
# your result agains the formula

def interest(value, rate, years):
    if years==0:
        return value
    else:
        return interest(value * (1 + rate), rate, years-1)

if __name__ == "__main__":
    years = int(input("Please enter an amaount of years: "))
    value = int(input("Please enter a initial value of the account: "))
    rate = float(input("Please enter the rate [%] "))
    rate=rate/100
    print(interest(value, rate, years))
