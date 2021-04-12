'''

Karen Sommer

CS 521 Spring 2021

Assignment 9

Problem 10 pages 564-566

'''
# In a supermarket, all vegetables have a product code, name, some description and price per unit.
# Design class lle vegetables to represent  vegetables. Provide to get and set methods for the class

class Vegetable:
    def __init__(self):
        self.code=0
        self.name=''
        self.description=''
        self.pricer_unit=0

    def get_code(self):
        return self.code
    def get_name(self):
        return self.name
    def get_description(self):
        return self.description
    def get_pricer_unit(self):
        return self.pricer_unit

    def set_code(self,new_code):
        self.code=new_code
    def set_name(self,new_name):
        self.name=new_name
    def set_description(self,new_description):
        self.description=new_description
    def set_pricer_unit(self,new_pricer_unit):
        self.pricer_unit=new_pricer_unit

    def __str__(self):
        return self.name+' with code ' + str(self.code)

v=Vegetable()
v.set_code(1234567890)
v.set_name('Carrot')
v.set_description('From California')
v.set_pricer_unit(2)

print(v.get_code())
print(v.get_name())
print(v.get_description())
print(v.get_pricer_unit())

print(v)
