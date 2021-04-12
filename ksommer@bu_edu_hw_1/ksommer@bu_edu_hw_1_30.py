'''

Karen Sommer

CS 521 Spring 2021

Assignment 3

Problem 30 and 154

'''

#Using the find method, write a short program that will print out the index of both 'o's
#when given the input 'Who's on first?

str="Who's on first?"
print(len(str))
#find(value, start)
index = 0
while index < len(str):
    # find return -1 when the substring is not found
    if str.find("o", index) == -1:
        break
    index = str.find("o", index)
    print("Index of o is:", index)
    index += 1
