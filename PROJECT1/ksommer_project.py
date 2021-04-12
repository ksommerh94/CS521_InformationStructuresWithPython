
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

def find_cities(c,country):
    '''
    Method: gives the option to the user to select an avaiable city and to view the hotels
    Input: the country selected , and the dictirionary of countries
    Output: cities from the specific country
    '''
    cities=country[c.upper()]
    #print(country[c.upper()])
    s="These are the cities in "+ c.upper()
    for i in cities.keys():
        s+='\n'
        s+=i
    print(s)
    flag_break_while=True
    while(flag_break_while):
        ans = (input('Do you want to check the hotels of one specific city? Y/N'))
        search_city=''
        print(ans.upper())
        if ans.upper()=='N':
            flag_break_while=False
            return (cities,search_city,False)
        elif ans.upper()=='Y':
            search_city = (input('Enter selected city from the list above:'))
            flag_break_while=False
            return (cities,search_city,True)
        else:
            print('Error in the selected option')

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


if __name__ == "__main__":

        flag=1
        #Load the file
        country=load_hotels(HOTELINFO_FILENAME)
        #asks for the country
        c=print_select_country(country)
        flag=True
        while flag:
            print("Now we can see hotel's information from "+ c.upper())
            print('''Select the number of the following options:
                    1) View all cities
                    2) View all hotels
                    3) Rank hotel
                    4) See top 10 best ranked selected country
                    5) Check price with promo codes
                    6) Change Country
                    7) Exit''')
            option = input()
            if  represents_int(option)==True:
                option=int(option)

                if option >7:
                    print('Option out of range')
                elif option ==7:
                    flag=False
                elif option==6:
                    r=print_select_country(country)
                elif option==1:
                    cities,search_city,selected_option=find_cities(c,country)
                    if selected_option==True:
                        extra_hotels_per_city(search_city,cities)
                elif option==2:
                    view_hotels(c,country)
                elif option==3:
                    cities,search_city,selected_option=find_cities(c,country)
                    #view_hotels(c,country)

            else:
                print('Option not valid')




        #search_country = (input(r))

        #find hotels of city

        #Display same hotels from all country with same AVG number base on the selected

        #check price of hotel with codes of discount

    #except: print('File not found or error occured')
