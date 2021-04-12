'''

Karen Sommer

CS 521 Spring 2021

Assignment 9

Problem 6 pages 564-566

'''
# Design a class for book such as an online retailer might want to keep track of the book.
class Book:
    def __init__(self,name,publisher,writer,price,ISBN,type,year):
        self.name=name
        self.publisher=publisher
        self.writer=writer
        self.price =price
        self.ISBN =ISBN
        self.type=type
        self.year=year

    def change_publisher(self,newPublisher):
        self.publisher=newPublisher

    def new_price(self,newPrice):
        self.price=newPrice

    def __str__(self):
        return "Book is:"+self.name+" by "+self.writer + " with a price of "+ str(self.price)+ "and published by " + self.publisher

b=Book('Rin Rin Renacuajo','Norma','Rafael Pombo',45000,'1234567890','Fabula',1890)
print(b)
b.new_price(45600)
print(b)
b.change_publisher('Santellana')
print(b)
