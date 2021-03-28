'''

Karen Sommer

CS 521 Spring 2021

Assignment 9

Problem 12 pages 564-566

'''
import random
# Create a class named 'Player' that initiates a player with default name as 'player', defualt level as 0 and default character
# type as 'default' . Create a function that compares two players and print the playaer name , level and character type that has the higher level
# If both characters are the same level print 'tie'. Create a main that compares 2 playes with random level from 1-99

class Player:
    def __init__(self,name,level=0,character_type='default'):
        self.level=level
        self.name=name
        self.character_type=character_type

    def compare(self,other_player):
        if self.level>other_player.level:
            return (self)
        elif self.level<other_player.level:
            return (other_player)
        else:
            return (0)

    def __str__(self):
        return 'The player '+self.name+' with ' + self.character_type+ ' is in level '+str(self.level)

level = random.randint(1, 99)
p1=Player('Yoshi',level,'ksommer')
level = random.randint(1, 99)
p2=Player('Peach',level,'gamer1')

print(p1)
print(p2)

player_compare=p1.compare(p2)
if player_compare==0:
    print('tie')
else:
    print('Better player is: ')
    print(player_compare)
