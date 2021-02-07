'''

Karen Sommer

CS 521 Spring 2021

Assignment 2

Problem 45 and 78


'''


#The world record in the 100-meter dash is 9.58 seconds, set by Usain Bolt.
#Write a program that prompts for a runner’s time in the 100 meter dash.
#Given that there are approximately 3.28 feet in a meter and
#5280 feet in a mile
#calculate and print the runner’s average speed in miles per hour.



print('Enter time of runner for 100 meters in seconds')
input_time = float(input())
#convert mts to miles - distance
mts_100_in_ft=328
ft_to_mile=mts_100_in_ft/5280
#print(ft_to_mile)

#convert seconds to hour - time
hour=input_time/3600
#print(hour)

#Avg speed=total distance/time
avg_speed=ft_to_mile/hour
print('The runner’s average speed in miles per hour is ',round(avg_speed,2), 'mph')
