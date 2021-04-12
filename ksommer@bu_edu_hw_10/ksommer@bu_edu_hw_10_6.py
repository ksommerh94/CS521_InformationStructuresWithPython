'''

Karen Sommer

CS 521 Spring 2021

Assignment 10

Problem 6 pages 610-613

'''
# In newtownian physisc , we know that 2 velocities in the same direction add to each other.
# In the opposite direction,  they substract from each other to give a net result in the direction of the bigger velocity.
# Design a simple class velocity aht has a field  tahtbhas  field for the speed (mts/sec)
# Writes a constructor that takes 3 parameters : distance , time , if velocity us in mts/sec or feet/sec
# constructor should take the feet/sec and transformt it to mts/sec
# Create overloaded unary  addition, substarct  operands for velocity


class Velocity:
    def __init__(self,distance,time,fts_per_sec):
        #one foot is 0.3048 meters
        if (fts_per_sec is True):
            #if the infromation is in feets per second
            mts=distance*0.3048
            self.speed=(mts/time)
        else:
            self.speed=(distance/time)

    def __add__(self, v2):
        return self.speed + v2.speed
    def __sub__(self, v2):
        return self.speed - v2.speed

a=Velocity(4,10,False)
b=Velocity(2,4,True)
print("Speed of A : "+ str(a.speed))
print("Speed of B : "+str(b.speed))
print(a+b)
print(a-b)
