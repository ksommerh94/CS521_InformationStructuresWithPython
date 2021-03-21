'''

Karen Sommer

CS 521 Spring 2021

Assignment 5

Problem 8 pages 416

'''
# write a function that takes a list as an argument and return a list that only
# contains items that occured exactly once in the original list

def uniqueList(list_int):
    return(list(set(list_int)))

if __name__ == "__main__":
    list_int=[0,1,5,2,90,55,34,56,32,11,90,0]
    print(uniqueList(list_int))
