'''

Karen Sommer

CS 521 Spring 2021

Assignment 4

Problem 22 pages 382-387

'''
#Given a list of integers, write in Python code to create a new list with same numbersf elements
#as the original listsucha that each integer in the new list is the sum of its neighbors and itself in the origial list.
#For example: if listA=[10,20,30,40,50] listB=[30,60,90,120,90]

listA=[10,20,30,40,50]
final_list=[]
for index,val in enumerate(listA):
    if index==0:
        final_list.append(val+listA[index+1])
    elif index == len(listA)-1:
        final_list.append(val+listA[index-1])
    else:
        final_list.append(val+listA[index+1]+listA[index-1])

print(final_list)
