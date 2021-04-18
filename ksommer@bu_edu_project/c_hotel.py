import copy
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
    def __str__(self):
        return ('Name Place: '+self.name +'\n' +'Service points: '+str(round(self.service,1)) +'\n'+'Location points: '+str(round(self.location,1)) +'\n'\
        +'Cleanliness points: '+str(round(self.cleanliness,1)) +'\n' +'Service Value: '+str(round(self.value,1)) +'\n') + 'Price: ' + str(self.__price) +'USD \n'


    def __copy__(self):
        return Hotel(self)
#PUBLIC METHOD
    def avg_ranks(self):
        '''
        Method: calculates the avg note the hotel has
        Input: none
        Output: the average value of the hotel taking into account ( service,location, cleanliness and value)
        '''
        return (round((self.service+self.location+self.cleanliness+self.value)/4,2))

    def new_service(self,other):
        self.service=(self.service+other)/2

    def new_location(self,other):
        self.location=(self.location+other)/2

    def new_cleanliness(self,other):
        self.cleanliness=(self.cleanliness+other)/2

    def new_value(self,other):
        self.value=(self.value+other)/2


#PRIVATE METHOD
    def __price_discount(self,code_discount):
        '''
        Method: Shows the price with a discount applied
        Input: The input code for check which discount should be applied
        Output: The price with the discount applied and a flag( if a the input code existed or not)
        '''
        flag=True
        if code_discount.upper()=='VACATIONS10':
            disc=self.__price*(0.1)
        elif code_discount.upper()=='TRAVEL50':
            disc=self.__price*(0.5)
        elif code_discount.upper()=='2021WORLD':
            disc=self.__price*(0.2)
        else:
            disc=0
            flag=False
        price_with_discount=self.__price-disc
        return (price_with_discount,flag)
