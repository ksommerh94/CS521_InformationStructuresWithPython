class Hotel():

    #contructor of experience class
    def __init__(self,name,service,location,cleanliness,value,breakfast,price):
        #Public attributes
        self.name=name
        self.service=service
        self.location=location
        self.cleanliness=cleanliness
        self.value=value
        self.breakfast=breakfast
        #Private attributes
        self.__price=price


    # printable representation of the experience object
    def __repr__(self):
        #print important information
        return repr('Name Place: '+self.name)

#PUBLIC METHOD
    def avg_ranks(self):
        '''
        Method: calculates the avg note the hotel has
        Input: none
        Output: the average value of the hotel taking into account ( service,location, cleanliness and value)
        '''
        return ((self.service+self.location+self.cleanliness+self.value)/4)

#PRIVATE METHOD
    def __price_discount(self,code_discount):
        '''
        Method: Shows the price with a discount applied
        Input: The input code for check which discount should be applied
        Output: The price with the discount applied and a flag( if a the input code existed or not)
        '''

        flag=True
        if code_discount.lower()=='VACATIONS10':
            disc=self.price*(0,1)
        elif code_discount.lower()=='TRAVEL50':
            disc=self.price*(0,5)
        elif code_discount.lower()=='2020WORLD':
            disc=self.price*(0,2)
        else:
            disc=0
            flag=False
        price_with_discount=self.price-disc
        return (price_with_discount,flag)
