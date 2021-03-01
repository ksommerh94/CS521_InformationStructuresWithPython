'''

Karen Sommer

CS 521 Spring 2021

Assignment 4

Problem 10 pages 307

'''
#Write a program that prompts for 3 numbers. Divide the first number by the second
# number and add that result to the thid. Using exceptions
#check for the following error ValueError and ZeroDivisionError


def max_min(list_int):
    return(min(list_int),max(list_int))

if __name__ == "__main__":
    try:
        n_1 = int(input("Please enter a number: "))
        n_2 = int(input("Please enter a number: "))
        n_3 = int(input("Please enter a number: "))
        print((n_1/n_2)+n_3)
    except ZeroDivisionError:
        print("Division by Zero!")
    except ValueError:
        print("Not valid number")
