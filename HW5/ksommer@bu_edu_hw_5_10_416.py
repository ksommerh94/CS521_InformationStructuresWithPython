'''

Karen Sommer

CS 521 Spring 2021

Assignment 5

Problem 10 pages 416

'''
# write a function that takes a list of integers as an argument and returns a tuple with the smallest and largest
# in the list. In case of a tie, either value is acceptable
def max_min(list_int):
    return(min(list_int),max(list_int))

if __name__ == "__main__":
    list_int=[0,1,5,2,90,55,34,56,32,11,90,0]
    print(max_min(list_int))
