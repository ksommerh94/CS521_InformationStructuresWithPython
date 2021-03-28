'''

Karen Sommer

CS 521 Spring 2021

Assignment 9

Problem 8 pages 564-566

'''
# Design a class for book such as an online retailer might want to keep track of the book.
class Medal:
    def __init__(self):
        self.name_athlete=''
        self.country=''
        self.event=''
        self.medal_type=''

    def get_name_athlete(self):
        return self.name_athlete
    def get_country(self):
        return self.country
    def get_event(self):
        return self.event
    def get_medal_type(self):
        return self.medal_type

    def set_name_athlete(self,new_name_athlete):
        self.name_athlete=new_name_athlete
    def set_country(self,new_country):
        self.country=new_country
    def set_event(self,new_event):
        self.event=new_event
    def set_medal_type(self,new_medal_type):
        self.medal_type=new_medal_type

    def __str__(self):
        return self.medal_type+' medal was won by:'+self.name_athlete+" from "+self.country + " on "+ self.event

m=Medal()
m.set_name_athlete('Karen Sommer')
m.set_country('Colombia')
m.set_event('Rugby')
m.set_medal_type('Gold')

print(m.get_name_athlete())
print(m.get_country())
print(m.get_event())
print(m.get_medal_type())
