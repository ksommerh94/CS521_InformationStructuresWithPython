'''

Karen Sommer

CS 521 Spring 2021

Assignment 10

Problem 4 pages 610-613

'''
# There are web pages that provide infromation about second-hand vehicles. Design a base class for vehicle
# with fields like model year , total mileage, VIN,EPA class, EPA mileage,engine, trasnmirion and option
#Design subclasses for car such as SUV, truck and minivan. think about sepcific fields and methods.

class Vehicle:
    def __init__(self,model_year,total_mileage,VIN,EPA_class,EPA_mileage,engine,transmitor,option):
        this.model_year=model_year
        this.total_mileage=total_mileage
        this.VIN=VIN
        this.EPA_class=EPA_class
        this.EPA_mileage=EPA_mileage
        this.engine=engine
        this.transmitor=transmitor
        this.option=option

class SUV(Vehicle):
    def __init__(self,model_year,total_mileage,VIN,EPA_class,EPA_mileage,engine,transmitor,option,style):
        super().__init__(self,model_year,total_mileage,VIN,EPA_class,EPA_mileage,engine,transmitor,option)
        self.style = style
    def num_row(self):
        print("2 rows of seats, sometimes 3.")

class Truck(Vehicle):
    def __init__(self,model_year,total_mileage,VIN,EPA_class,EPA_mileage,engine,transmitor,option,number_trailers):
        super().__init__(self,model_year,total_mileage,VIN,EPA_class,EPA_mileage,engine,transmitor,option)
        self.number_trailers = number_trailers
    def used_for(self):
        print('Hauling')

class Minivan(Vehicle):
    def __init__(self,model_year,total_mileage,VIN,EPA_class,EPA_mileage,engine,transmitor,option,doors_slide):
        super().__init__(self,model_year,total_mileage,VIN,EPA_class,EPA_mileage,engine,transmitor,option)
        self.doors_slide = doors_slide
    def feature(self):
        print("They usually have an extra row of seats to haul people that will often fold down for extra cargo space.")
