from c_place import Place
from c_main_place import Mainplace

def read_fill(dict_city):
    '''
    Method: Read text file and fill dictionary
    Input: empty dictionary
    Output: full dictionary with the texts information
    '''
    try:

        read_text=[]
        #Read text file
        f = open("input_text.csv", "r")
        f_read=f.readlines()
        for f in (f_read):
            read_text.append(f.split(';'))

        #keep record of the main Place
        mainp=Null
        for index,texto in enumerate(read_text):
            if index==0:
                emp=[]
                mp=Mainplace(texto[0],texto[1],texto[2],texto[3],texto[6],texto[4],texto[5],emp)
                #save the main place in 'big' variable
                mainp=mp
            else:
                list_days=[]
                for i in range(8,len(texto)-1):
                    list_days.append(texto[i])
                #create the place and list of days to the place
                p=Place(texto[1],texto[2],texto[3],texto[4],texto[5],texto[6],texto[7],list_days)
                # add the place to the main place , make the connection
                mainp.__place.append(p)



    except:
        pass

    return mainp

if __name__ == "__main__":
    try:
        dict_city=read_fill(dict_city={})
    except:
        print('File not found or error occured')
