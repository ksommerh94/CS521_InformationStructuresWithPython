class Mainplace():

    #contructor of experience class
    def __init__(self,name,trip_type,people,days,tips,arrival,departure,place):
        #Public attributes
        self.name=name
        self.trip_type=trip_type
        self.people=people
        self.days=days
        self.arrival=arrival
        self.departure=departure
        self.tips=arrival
        #Private attribute
        self.__place=place

    # printable representation of the experience object
    def __repr__(self):

        return repr('Main place: '+self.name+ '   Type of trip: '+self.trip_type + '  Days: '+ self.days  )
