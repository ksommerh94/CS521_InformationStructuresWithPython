'''

Karen Sommer

CS 521 Spring 2021

Assignment 4

Problem 14 pages 264-267

'''
#You by an international calling card to India. The calling card company has some special offers
# a) if you charge your card with 5 or 10 you dont get any extra
# b) For a $25 charge, you get $3 extra
# c) For a $50 charge, you get $8 extra
# d) For a $100 charge, you get $20 extra
# write a function that asks the user for the amaunt she wants on the card, and returns the total
# charge that the user gets.

def recharge(amount):
    if amount ==5 or amount == 10:
        return (amount)
    elif amount==25:
        return(amount+3)
    elif amount==50:
        return(amount+8)
    elif amount==100:
        return(amount+20)
    else:
        return('Invalid Amount')

if __name__ == "__main__":
    amount = int(input("Amount to add to the card: "))
    print('New credit in card:$', recharge(amount) )
