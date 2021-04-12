'''

Karen Sommer

CS 521 Spring 2021

Assignment 10

Problem 10 pages 610-613

'''
# Design a class called color.
# The fields of the class are three decimal for red, green ,and blue components in the range of 0 to 1 inclusive
#(0 indicates black and 1 indicates white)
#Add checks to ensure that the values are always in the given range.
#provide addition and subtraction operators for the color class.
# include saturation in the addition and substraction:
#if any component goes less than 0 or greater than 1 assign them 0 or 1 respectively


class Color:
    def __init__(self,red,green,blue):
        if (red<0 or red >1 or blue<0 or blue >1 or green<0 or green >1 ):
            print('ERROR, color out of range')
        else:
            if red >= 0 and red <= 1:
                self.red=red
            if green >= 0 and green <= 1:
                self.green=green
            if blue >= 0 and blue <= 1:
                self.blue=blue
    def __str__(self):
        return "Red:"+str(self.red) + " Green "+ str(self.green) +" Blue "+str(self.blue)

    def get_red(self):
        return self.red
    def get_blue(self):
        return self.blue
    def get_green(self):
        return self.green

    def __add__(self,other_color):
        try:
            new_red=round(self.red+other_color.red,2)
            new_blue=round(self.blue+other_color.blue,2)
            new_green=round(self.green+other_color.green,2)
            if new_red > 1:
                new_red=1
            elif new_blue >1:
                new_blue=1
            elif new_green >1:
                new_green=1
            max_color=max(new_red,new_blue,new_green)
            min_color=min(new_red,new_blue,new_green)
            saturation=(max_color-min_color) / (max_color+min_color)
            print("Saturation Addition: ",str(saturation))
            new_Color=Color(new_red,new_green,new_blue)
            return new_Color
        except:
            print("Error in Addition")

    def __sub__(self,other_color):
        try:
            new_red=round(self.red-other_color.red,2)
            new_blue=round(self.blue-other_color.blue,2)
            new_green=round(self.green-other_color.green,2)

            if new_red < 0:
                new_red=0
            elif new_blue < 0:
                new_blue=0
            elif new_green < 0:
                new_green=0
            max_color=max(new_red,new_blue,new_green)
            min_color=min(new_red,new_blue,new_green)
            saturation=(max_color-min_color) / (max_color+min_color)
            print("Saturation Substraction: ",str(saturation))
            new_Color=Color(new_red,new_green,new_blue)
            return new_Color
        except:
            print("Error in substraction")



c1=Color(0.2,0.3,0.8)
c2=Color(0.3,0.1,0.3)

add_color=c1+c2
sub_color=c1-c2

print(add_color)
print(sub_color)
