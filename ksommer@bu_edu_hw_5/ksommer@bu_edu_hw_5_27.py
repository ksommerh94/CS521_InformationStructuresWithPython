'''

Karen Sommer

CS 521 Spring 2021

Assignment 5

Problem 27 pages 264-267

'''
#A hapax legomenon ( often abbreviated to hapax) is a word wich occurs only once
#in a docuement. In the fields of computational linguistics and natural language processing
# it is common to disregard hapax legomena (and sometimes, other infrequent words)
# as they are likley to have little value for computational techniques. This disregard has added benefit
# of significant reducing the memory use of an application.
# Define a function that given the file name of a text will return all it
# hapaxes. Make sure your prrogram ignores capitalizations

def count_words(file):
    dict={}
    for line in file:
        for word in line.split():
            print(word)
            if word.isalpha():

                if word.lower() in dict.keys():
                    dict[word.lower()]+=1
                else:
                    dict[word.lower()]=1

    min_val = min(dict.values())
    #print(min_val)
    res =[]
    for keys,values in dict.items():
        if values == min_val:
            res.append(keys)
    return(res)



if __name__ == "__main__":
    try:
        print ('Enter a text file name')
        text = (input())
        f = open(text, "r")
        print(count_words(f))
        f.close()
    except:
        print('File not found')
    #print(f.read())
