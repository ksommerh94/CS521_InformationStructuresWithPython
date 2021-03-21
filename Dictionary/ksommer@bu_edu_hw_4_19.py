'''

Karen Sommer

CS 521 Spring 2021

Assignment 4

Problem 19 pages 476-479

'''
# Create a dictionary or the months the calendar.
# Keys are the names of the months
#and the values the number of days in the month

import calendar

calendar_dict={}
keys_list=[]
values_list=[]
for i in range(1,13):
    keys_list.append(calendar.month_name[i])
    values_list.append(calendar.monthrange(2021, i)[1])

calendar_dict = dict(zip(keys_list, values_list))
print('Days for the moths in 2021',calendar_dict)
