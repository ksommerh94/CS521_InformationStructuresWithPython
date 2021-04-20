'''

Karen Sommer

CS 521 Spring 2021

Assignment 11

Problem 1-8 pages 641

'''
import random

def print_grid(grid):
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            print(grid[i][j], end=' ')
        print()
    print()

class Animal:
    #Exercise 6 , init animals can be inefficient , especially if e island is quite full
    def __init__(self,pos_x,pos_y,starve_time,breeding_time):
        self.pos_x=pos_x
        self.pos_y=pos_y
        self.starve_time=starve_time
        self.breeding_time=breeding_time
    def move(self):
        # Exercise 1 : add randomness to the direction to move
        possible_moves=[(0,1),(0,-1),(1,0),(-1,0),(1,1),(1,-1),(-1,-1),(-1,1)]
        random_move=random.choice(possible_moves)
        new_x= self.pos_x + random_move[0]
        new_y= self.pos_y + random_move[1]

    def move_away_two_hops(self,grid):
        # Exercise 3: Add the ability to look in 2 hop , and move up or forward depending on the situation
        # Exercise 8: Implement one of the move miprovements : list
        '''
        method: move away in 1 step if there is a P in the first ring or second hop of distance
                get closer one step if there is a Y in the first ring or second hop of distance
        input: the grid
        output: none
        '''
        possible_moves=[(0,1),(0,-1),(1,0),(-1,0),(1,1),(1,-1),(-1,-1),(-1,1),\
                        (0,2),(0,-2),(1,2),(2,2),(2,1),(2,0),(2,-1),(2,-2),(1,-2),(-1,-2),(-2,-2),(-2,-1),(-2,0),(-2,1) ,(-2,2),(-1,2)]
        for pm in possible_moves:
            if self.pos_x +pm[0]< len(grid) and self.pos_y+pm[1] < len(grid) and self.pos_x +pm[0]>=0 and self.pos_y+pm[1] >=0:
                if  grid[ self.pos_x +pm[0] ][ self.pos_y+pm[1] ] =='P':
                    #if is a predator, get away
                    # in x
                    if pm[0]==0:
                        new_x=0
                    elif pm[0]>0:
                        new_x=-1
                    else:
                        new_x=1
                    # in y
                    if pm[1]==0:
                        new_y=0
                    elif pm[1]>0:
                        new_y=-1
                    else:
                        new_y=1

                    if (self.pos_x+new_x>=0 and self.pos_x+new_x<len(grid) ) and  (self.pos_y+new_x>=0 and self.pos_y+new_x<len(grid) ):
                        if grid[self.pos_x+new_x][self.pos_y+new_y]=='_':
                            grid[self.pos_x][self.pos_y]='_'
                            self.pos_x=self.pos_x+new_x
                            self.pos_y=self.pos_y+new_y
                            grid[self.pos_x][self.pos_y]=self.char_grid
                            break
                elif  grid[ self.pos_x +pm[0] ][ self.pos_y+pm[1] ] =='Y':
                    #if is a predator, get closer 1 step
                    # in x
                    if pm[0]==0:
                        new_x=0
                    elif pm[0]>0:
                        new_x=1
                    else:
                        new_x=-1
                    # in y
                    if pm[1]==0:
                        new_y=0
                    elif pm[1]>0:
                        new_y=1
                    else:
                        new_y=-1

                    if (self.pos_x+new_x>=0 and self.pos_x+new_x<len(grid) ) and  (self.pos_y+new_x>=0 and self.pos_y+new_x<len(grid) ):
                        if grid[self.pos_x+new_x][self.pos_y+new_y]=='_':
                            grid[self.pos_x][self.pos_y]='_'
                            self.pos_x=self.pos_x+new_x
                            self.pos_y=self.pos_y+new_y
                            grid[self.pos_x][self.pos_y]=self.char_grid
                            break

    def survival_starve_quick(self):
        self.starve_time=self.starve_time-1

    def survival_reproduce_quick(self):
        self.breeding_time=self.breeding_time-1

class Prey(Animal):
    def __init__(self,pos_x,pos_y,starve_time,breeding_time):
        super().__init__(pos_x,pos_y,starve_time,breeding_time)
        self.char_grid='Y'

    def move_away(self,grid):
        # Exercise 2 move away from neighnor predator
        '''
        method: move away if there is a P in the first ring of distance
        input: the grid
        output: none
        '''
        possible_moves=[(0,1),(0,-1),(1,0),(-1,0),(1,1),(1,-1),(-1,-1),(-1,1)]
        for pm in possible_moves:
            if  grid[ self.pos_x +pm[0] ][ self.pos_y+pm[1] ] =='P':
                new_x= (pm[0] ) * -1
                new_y= (pm[1] ) * -1
                if (self.pos_x+new_x>=0 and self.pos_x+new_x<len(grid) ) and  (self.pos_y+new_x>=0 and self.pos_y+new_x<len(grid) ):
                    grid[self.pos_x][self.pos_y]='_'
                    self.pos_x=self.pos_x+new_x
                    self.pos_y=self.pos_y+new_y
                    grid[self.pos_x][self.pos_y]='Y'
                    break


class Predator(Animal):
    def __init__(self,pos_x,pos_y,starve_time,breeding_time):
        super().__init__(pos_x,pos_y,starve_time,breeding_time)
        self.char_grid='P'
        breeding_time=2

#Exercise 7 : test the code to determin situations in which multiple  moves can ocurr
grid_location=[['_' for x in range(5)] for y in range(5)]

p1=Predator(0,1,4,6)
grid_location[0][1]=p1.char_grid

p2=Predator(3,2,4,6)
grid_location[3][2]=p2.char_grid

y1=Prey(2,3,2,9)
grid_location[2][3]=y1.char_grid
print('Initial location')
print_grid(grid_location)
print('----------------')
y1.move_away_two_hops(grid_location)
print('after prey moves')
print_grid(grid_location)
p1.move_away_two_hops(grid_location)
print('after predator 1 moves')
print_grid(grid_location)
p2.move_away_two_hops(grid_location)
print('after predator 2 moves')
print_grid(grid_location)

#Survivial rules
# Exercise 4
p1.survival_starve_quick()
y1.survival_reproduce_quick()
