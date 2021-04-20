'''

Karen Sommer

CS 521 Spring 2021

Assignment 11

Problem 1 pages 684

'''
# importing csv module
import csv

def print_file(rows):
    for row in rows:
        print(', '.join(c for c in row))

def delete_row(rows,index=1):
    if len(rows)>1:
        rows.pop(index)
    else:
        print('Unable to delete')

def delete_column(rows,index=1):
    #print(len(rows))
    if len(rows)>1:
        for col in rows:
            del col[index]
    else:
        print('Unable to delete')

def insert(rows):
    insert_data=['Nick Jonas,November']
    rows.insert(1, insert_data)

def insert_col(rows):
    print('INSERT COLUMN')
    for counter,col in enumerate(rows):
        if counter==0:
            col.insert(2,'age')
        else:
            col.insert(2,str(20+counter))

def change_value_cell(rows):
    rows[2][0]='Karen Sommer'

def save_file(rows):
    with open('hw_11_output.csv', mode='w') as output_file:
        output_writer = csv.writer(output_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        for row in rows:
            output_writer.writerow(row)


# csv file name
filename = "hw_11.csv"
rows = []
# reading csv file
try:
    with open(filename, 'r') as csvfile:
        # creating a csv reader object
        csvreader = csv.reader(csvfile)
        for row in csvreader:
            rows.append(row)
    flag=True
    while flag:
        print('''\nSelect the action:
                p for print data
                d for delete row
                i for insert column
                c for change value in cell
                o for output the data in csv
                e for exit\n''')
        option = input()
        if option.lower() =='e':
            flag=False
        elif option.lower() =='p':
            print_file(rows)
        elif option.lower() =='d':
            delete_row(rows)
        elif option.lower()=='i':
            insert_col(rows)
        elif option.lower() == 'c':
            change_value_cell(rows)
        elif option.lower() =='o':
            save_file(rows)
        else:
            print('unknown error')
except:
    print('File not found')
