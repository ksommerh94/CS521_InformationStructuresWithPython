
'''
Dictionary country
        as key -->  country , as value --> dictionary of cities
                                                as key -->  city , as value --> list of hotels

'''
from c_hotel import Hotel
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

if __name__ == "__main__":
    try:
        country=load_hotels(HOTELINFO_FILENAME)
        print(country)

        #find hotels of city

        #Display same hotels from all country with same AVG number base on the selected

        #check price of hotel with codes of discount

    except:
        print('File not found or error occured')
