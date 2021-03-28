
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
            if search_country.lower() == i.lower():
                while_flag=False
        if while_flag==True:
            print('Country not found!')
    return(search_country.lower())

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
    Output: None
    '''
    cities=country[c.capitalize()]
    #print(country[c.capitalize()])
    s="These are the cities in "+ c.capitalize()
    for i in cities.keys():
        s+='\n'
        s+=i
    #s+='\n'
    print(s)
    ans = (input('Do you want to check the hotels of one specific city? Y/N'))
    print(ans)
    if ans.lower()=='n':
        return
    elif ans.lower()=='y':
        while_flag=True
        while while_flag:
            search_city = (input('Enter selected city:'))
            if search_city.capitalize() in cities.keys():
                lhotels=cities[search_city.capitalize()]
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
    else:
        print('Error in the selected option')



if __name__ == "__main__":

        flag=1
        #Load the file
        country=load_hotels(HOTELINFO_FILENAME)
        #asks for the country
        c=print_select_country(country)
        flag=True
        while flag:
            print("Now we can see hotel's information from "+ c.capitalize())
            print('''Select the number of the following options:
                    1) View all cities
                    2) View all hotels
                    3) Rank hotel
                    4) See best ranked
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
                    find_cities(c,country)
                elif option==2:
                    view_hotels(c,country)

            else:
                print('Option not valid')




        #search_country = (input(r))

        #find hotels of city

        #Display same hotels from all country with same AVG number base on the selected

        #check price of hotel with codes of discount

    #except: print('File not found or error occured')
