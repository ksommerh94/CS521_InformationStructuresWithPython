class Place():

    #contructor of experience class
    def __init__(self,name,arrival,hotel,h_comodidad,h_limpieza,h_limpieza_b,h_facilities,list_day):
        #Public attributes
        self.name=name
        self.arrival=arrival
        self.hotel=hotel
        self.h_comodidad=h_comodidad
        self.h_limpieza=h_limpieza
        self.h_limpieza_b=h_limpieza_b
        self.h_facilities=h_facilities
        #Private attributes
        self.__list_day=list_day


    # printable representation of the experience object
    def __repr__(self):
        #print important information
        return repr('Nombre lugar: '+self.name+ '   Modo de llegada: '+self.arrival + '  Hotel: '+ self.hotel + '  Activity: '+ self.__list_day)
