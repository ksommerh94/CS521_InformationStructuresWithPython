'''

Karen Sommer

CS 521 Spring 2021

Assignment 5

Problem 11 pages 416

'''
# Write a function named safe_input(prompt, type) that works like the python safe_input
#function , except that it only accepts the specified tupe of input.
#the function takes 2 arguments
# prompt : string
# type: int, float, string
# the function will keep prompting for input until correct inpur of the specified type eneteres.
# the function return the input. If the input was specified to be a number
#(float or int), the value returned will be of the correcct type, that is the function will perform the conversion
# The default for a prompt is the empty string. The default for the tyrpe is string.

def safe_input(prompt, type):
    flag=False
    value=None
    if type=='number' and (prompt.isdigit() or prompt.replace('.', '', 1).isdigit()) :
        if prompt.isdigit():
            value=int(prompt)
            flag=True
        else:
            value=float(prompt)
            flag=True
    elif type=='string':
        if (prompt.isdigit() or prompt.replace('.', '', 1).isdigit()) :
            pass
        else:
            value=(prompt)
            flag=True

    return(flag,value)

valid_type=['number','string','']
if __name__ == "__main__":
    type = (input("Please enter type of input(number or string): "))
    if type.lower() in valid_type:
        if type =='':
            type='string'
        else:
            type=type.lower()
        flag=False
        while flag==False:
            prompt = (input("Please enter your input: "))
            flag,value=safe_input(prompt, type)
        print(value)
    else:
        print('Check the input type you entered')
