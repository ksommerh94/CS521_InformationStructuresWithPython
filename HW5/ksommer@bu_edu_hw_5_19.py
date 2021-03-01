'''

Karen Sommer

CS 521 Spring 2021

Assignment 4

Problem 19 pages 264-267

'''
import datetime
#Write a function that takes as input a string that scores date and time (24 hour clock)
# in the following format MM/DD/YYYY HH:MM:SS and prints the following
# a) DD/MM/YYYYY
# b) HH:MM:SS
# c) MM/YYYY
# d) Whether the time is AM or PM

def date_print(date_string_value):
    date_time_obj = datetime.datetime.strptime(date_string_value, '%m/%d/%Y %H:%M:%S')
    print('The date in the format DD/MM/YYYY is',date_time_obj.strftime('%d/%m/%Y'))
    print('The date in the format HH:MM:SS is',date_time_obj.time())
    print('The date in the format MM/YYYY is',date_time_obj.strftime('%m/%Y'))
    if date_time_obj.hour <12:
        print('The time is AM')
    else:
        print('The time is PM')

if __name__ == "__main__":
    date_string_value ='12/31/2021 23:45:01'
    date_print(date_string_value)
