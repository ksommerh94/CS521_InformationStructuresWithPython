'''

Karen Sommer

CS 521 Spring 2021

Assignment 10

Problem 8 pages 610-613

'''
# Design a class called TextDocuemnt that reads the content of a file text only.
# create a constructor that takes the path of a text file. Create an overload addition for this class that adds ( concatenates)
# 2 TextDocuemnt objects Appends the second to the end of the first one and createx new text file.

class TextDocuemnt:
    def __init__(self,path):
        try:
            read_text=[]
            #Read text file
            f = open(path, "r")
            data = f.read()
            self.data=data
        except:
            print('FILE NOT FOUND')


    def __add__(self, other_text):
        try:
            file = open("AddTextHere.txt", "w")
            file.write(self.data+other_text.data)
            file.close()
            return file
        except:
            print('ERROR')
        #return self.speed + v2.speed
path1='input_t12.csv'
path2='input_t2.csv'
t1=TextDocuemnt(path1)
t2=TextDocuemnt(path2)
print("ADDING TEXT")
t1+t2
