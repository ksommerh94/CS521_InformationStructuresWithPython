'''

Karen Sommer

CS 521 Spring 2021

Assignment 4

Problem 8 pages 476-479

'''
# If my_dict={'a':15,'c':35,'b':20}, write Pytho code:
# a) To print all keys                          b) to print all values
# c) To print all keeys and values pair         d) To print all keys and values pair in order of key
# e) To print all keeys and values pair in order of values

my_dict={'a':15,'c':35,'b':20}

#A)
print('A:To print all keys')
for dict in my_dict.items() :
    print ('Key',dict[0])
#B)
print('B:To print all values')
for dict in my_dict.items() :
    print ('Values',dict[1])
#C)
print('C:To print all keys and values pair')
for key, value in my_dict.items() :
    print ('Key',key,'Value', value)
#D)
print('D:To print all keys and values pair in order of key')
sorted_dict_key = sorted(my_dict.items())
for key, value in sorted_dict_key:
    print ('Key',key,'Value', value)
#E)
print('E:To print all keys and values pair in order of values')
sorted_values = sorted(my_dict.values()) # Sort the values
sorted_my_dict = {}
for i in sorted_values:
    for k in my_dict.keys():
        if my_dict[k] == i:
            sorted_my_dict[k] = my_dict[k]
            break
for key, value in sorted_my_dict.items() :
    print ('Key',key,'Value', value)
