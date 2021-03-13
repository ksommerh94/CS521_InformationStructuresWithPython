class Experience():

    #contructor of experience class
    def __init__(self,activity,value,day):
        #Public Attributes
        self.activity=activity
        self.value=value
        #private attribute
        self.__day=day

    # printable representation of the experience object
    def __repr__(self):
        return repr('Activity: '+self.activity+ '   Value USD: $'+self.value + '  Days: '+ self.__day)
