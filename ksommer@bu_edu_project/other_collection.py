'''
Here are the tuples and the set. These two collections arent part of my project.
That is why I have them here in a diffrent section
'''
#-------------------------tuples----------------------
#tuple 1
print('------TUPLE------')
t1 = ('Prof. Pinsky', 'CS521', 'spring 2021', 'in person class')
#slicing
print(t1[2:])
#tuple 2
t2 = ('python', 'boston','met','college')
new_input=('university',)
#add new value to tuple 2
t2 += new_input
new_tuple=t1+t2
#print new tuple
print(new_tuple)

#Loop over the final tuple
for count,nt in enumerate( new_tuple):
    if count==0:
        print(nt.upper())
    elif nt =='boston':
        print(nt.upper())
    elif nt =='university':
        print(nt.upper())

#-------------------------set----------------------
#set 1
print('------SET------')
s1 = {'Prof. Pinsky', 'MET','Boston', 'Spring',2021,True}
#add element to set 1
s1.add('In person class')
print(s1)
#try to add an exisiting element
print('Trying to add an exisiting string')
s1.add('MET')
print(s1)
#remove specific element
print('Remove 2021 element')
s1.remove(2021)
print(s1)
#Clear set 1
print('Clear set')
s1.clear()
print(s1)
