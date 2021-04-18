
'''
Dictionary country
        as key -->  country , as value --> dictionary of cities
                                                as key -->  city , as value --> list of hotels

'''
from c_hotel import Hotel
from texttable import Texttable

HOTELINFO_FILENAME = "input_v2.csv"

def load_hotels(HOTELINFO_FILENAME):
    '''
    Method: Read text file and fill country dictionary with the nested dictionary and list
    Input: nothing
    Output: full dictionary the nested dictionary and list
    '''
    try:
        read_text=[]
        #Read text file
        f = open(HOTELINFO_FILENAME, "r")
        f_read=f.readlines()
        for f in (f_read):
            read_text.append(f.split(','))

        country={}
        for index,texto in enumerate(read_text):
            if index!=0:
                # Get information from text file

                pais=texto[0]
                ciudad=texto[1]
                # Hotel infromation from text file
                name=texto[2]
                service=int(texto[3])
                location=int(texto[4])
                cleanliness=int(texto[5])
                value=int(texto[6])
                breakfast=False
                if texto[7]=='t':
                    breakfast=True
                price=int(texto[8])

                if pais not in country.keys():
                    city={}
                    list_hotel=[]
                    # create hotel
                    hotel=Hotel(name,service,location,cleanliness,value,breakfast,price)
                    list_hotel.append(hotel)
                    # add hotel list to city
                    city[ciudad]=list_hotel
                    # add city  to country
                    country[pais]=city
                else:
                    if ciudad not in country[pais].keys():
                        list_hotel=[]
                        # create hotel
                        hotel=Hotel(name,service,location,cleanliness,value,breakfast,price)
                        list_hotel.append(hotel)
                        # add hotel list to city
                        city[ciudad]=list_hotel
                    else:
                        #add hotel to city list
                        hotel=Hotel(name,service,location,cleanliness,value,breakfast,price)
                        city[ciudad].append(hotel)
    except:
        pass

    return country

def print_select_country(country):
    '''
    Method: Gives to the user a list of countries for selection
    Input: dictionary of whole data
    Output: the selected country
    '''
    while_flag=True
    while while_flag:
        s="Please set the country you want to check from the list below:"
        for i in country.keys():
            s+='\n'
            s+=i
        #s+='\n'
        print(s)
        search_country = (input('Enter selected country:'))
        for i in country.keys():
            if search_country.upper() == i.upper():
                while_flag=False
        if while_flag==True:
            print('Country not found!')
    print(search_country)
    return(search_country.upper())

def represents_int(s):
    '''
    Method: check if string is a integer or not, for the selected options
    Input: string ( input)
    Output: true or false, if the string is a valid integer/ option or not
    '''
    try:
        int(s)
        return True
    except ValueError:
        return False

def extra_hotels_per_city(search_city,cities):
    '''
    Method: prints all hotel from a city
    Input: the target city (search_city) and the city dictionary (cities)
    Output: None
    '''
    while_flag=True
    while while_flag:
        if search_city.upper() in cities.keys():
            lhotels=cities[search_city.upper()]
            table = Texttable()
            table.header(['Hotel','Service','Location','Cleanliness','Value','Breakfast'])
            for h in lhotels:
                b='No'
                if h.breakfast==True:
                    b='Yes'
                table.add_row([h.name,h.service, h.location,h.cleanliness,h.value,b])
            print(table.draw())
            while_flag=False
        else:
            print('City entered not found!')

def view_hotels(c,country):
    '''
    Method: Print all the hotel of a country
    Input: the country selected c , and the dictirionary of countries county
    Output: None
    '''
    cities=country[c.upper()]
    #print(cities)
    for loop_cities in cities.keys():
        print(loop_cities)
        lhotels=cities[loop_cities.upper()]
        table = Texttable()
        table.header(['Hotel','Service','Location','Cleanliness','Value','Breakfast'])
        for h in lhotels:
            b='No'
            if h.breakfast==True:
                b='Yes'
            table.add_row([h.name,h.service, h.location,h.cleanliness,h.value,b])
        print(table.draw())

def view_citites(c,country):
    '''
    Method: prints all the cities in the country
    Input: the country selected , and the dictirionary of countries
    Output: None
    '''
    cities=country[c.upper()]
    #print(country[c.upper()])
    s="These are the cities in "+ c.upper()
    for i in cities.keys():
        s+='\n'
        s+=i
    print(s)

def select_hotel(hotels,search_city):
    outter_flag=True
    while outter_flag:
        s="These are the hotels in "+ search_city.upper()
        cities=country[c.upper()]
        for count, hotel in enumerate(hotels):
            print('No.'+ str(count+1) + ' : ' + hotel.name  )
        selected_idhotel = int(input('Enter the number of the Hotel or 0(zero) for exit'))
        #print(len(hotels))
        if selected_idhotel==0:
            outter_flag=False
        elif selected_idhotel-1<len(hotels):
            inner_flag=True
            while inner_flag:
                selected_hotel=hotels[selected_idhotel-1]
                print(selected_hotel)
                print('''\nSelect the number of the following options:
                        1) Check price with code
                        2) Rate hotel
                        3) Get average score
                        4) Exit \n''')
                option = input()
                if  represents_int(option)==True:
                    option=int(option)
                    if option >4:
                        print('Option out of range')
                    elif option ==4:
                        outter_flag=False
                        inner_flag=False
                    elif option==1:
                        hotel_code(selected_hotel)
                    elif option==3:
                        print ('The average score od this hotel is :'+str(selected_hotel.avg_ranks())+'\n')
                    elif option==2:
                        rate_hotel(selected_hotel)
        else:
            print('The selected ID does not exist')

def select_hotel_city(c,country):
    '''
    Method: gives the option to the user to select an avaiable city and to view the hotels
    Input: the country selected , and the dictirionary of countries
    Output: cities from the specific country
    '''
    flag=True
    while flag:
        s="These are the cities in "+ c.upper()
        cities=country[c.upper()]
        for i in cities.keys():
            s+='\n'
            s+=i
        print(s)
        search_city = (input('For select a hotel, please first enter a city from the aboves list:'))
        if search_city.upper() in cities.keys():
            #print(cities[search_city.upper()])
            flag=False
            select_hotel(cities[search_city.upper()],search_city)
        else:
            print('City entered not valid')

def hotel_code(selected_hotel):
    print('Enter code')
    discount_code = input()
    price_with_discount,code_exist=selected_hotel._Hotel__price_discount(discount_code)
    if code_exist==False:
        print('The code '+discount_code+' does not exist')
    else:
        print('Price with discount would be $'+str(price_with_discount) + 'USD \n')

def rate_hotel(selected_hotel):
    flag=True
    while flag:
        print('\nYou have to rate only with this numbers: 1, 2, 3, 4 or 5')
        service = (input('Rate the service'))
        location = (input('Rate the location'))
        cleanliness = (input('Rate the cleanliness'))
        value = (input('Rate the value'))

        if  represents_int(service)==True and represents_int(location)==True and represents_int(cleanliness)==True and represents_int(value)==True:
            if  (int(service)<6 and int(service)>0 and \
                 int(location)<6 and int(location)>0 and  \
                 int(cleanliness)<6 and int(cleanliness)>0 and \
                 int(value)<6 and int(value)>0 ):
                 selected_hotel.new_service(int(service))
                 selected_hotel.new_location(int(location))
                 selected_hotel.new_cleanliness(int(cleanliness))
                 selected_hotel.new_value(int(value))
                # print(selected_hotel)
                 flag=False
                 break
            else:
                print('Input out of range')

        else:
            print('Error on the input')





if __name__ == "__main__":

        flag=1
        #Load the file
        country=load_hotels(HOTELINFO_FILENAME)
        #asks for the country
        c=print_select_country(country)
        print(c.upper())
        flag=True
        while flag:
            print('------------------------------------------------------')
            print("Now we can see hotel's information from "+ c.upper())
            print('''\nSelect the number of the following options:
                    1) View all cities
                    2) View all hotels
                    3) Select a hotel
                    4) Change Country
                    5) Exit\n''')
            option = input()
            if  represents_int(option)==True:
                option=int(option)
                if option >5:
                    print('Option out of range')
                elif option ==5:
                    flag=False
                elif option==4:
                    c=print_select_country(country)
                elif option==1:
                    view_citites(c,country)
                elif option==2:
                    view_hotels(c,country)
                elif option==3:
                    select_hotel_city(c,country)
            else:
                print('Option not valid')




        #search_country = (input(r))

        #find hotels of city

        #Display same hotels from all country with same AVG number base on the selected

        #check price of hotel with codes of discount

    #except: print('File not found or error occured')
