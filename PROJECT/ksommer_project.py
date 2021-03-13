from c_experience import Experience


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
            read_text.append(f.split(','))
        for index,texto in enumerate(read_text):
            list_exp=[]
            # validate to add to dictionary
            if texto[0] not in dict_city.keys():
                #create object Experience and add to list
                exp=Experience(texto[1],texto[2],texto[3].replace("\n", ""))
                list_exp.append(exp)
                #add list as value of the dictionary
                dict_city[texto[0]]=list_exp
            else:
                #create object Experience and add to existed list
                exp=Experience(texto[1],texto[2],texto[3].replace("\n", ""))
                dict_city[texto[0]].append(exp)
    except:
        pass

    return dict_city

if __name__ == "__main__":
    try:
        dict_city=read_fill(dict_city={})
    except:
        print('File not found or error occured')
