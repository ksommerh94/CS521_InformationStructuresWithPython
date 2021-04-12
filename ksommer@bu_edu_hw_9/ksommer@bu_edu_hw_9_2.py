'''

Karen Sommer

CS 521 Spring 2021

Assignment 9

Problem 2 pages 564-566

'''
# Write a shopping cart class to implement  a shopping cart  that you often find on websites
# Think about what things you could store in a cart and also what operations you could perform on the cart

class ShoppingCart:
    def __init__(self,dict_things):
        self.things=dict_things
        self.fp=self.checkout()

    def checkout(self):
        final_price=0
        for key,val in self.things.items():
            quantity,price=val
            final_price+=(quantity*price)
        return final_price

    def __str__(self):
        return "The final price of the purchase is:"+str(self.fp)

stuff={'Ipod':(1,450),'Tv':(2,390),'Chromecast':(5,50)}
sc=ShoppingCart(stuff)
stuff2={'Ipod':(6,450),'Tv':(1,100),'Chromecast':(3,25)}
sc2=ShoppingCart(stuff2)

print(sc)
print(sc2)
