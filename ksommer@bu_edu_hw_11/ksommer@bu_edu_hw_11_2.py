'''

Karen Sommer

CS 521 Spring 2021

Assignment 11

Problem 2 pages 685

'''

import os
import shutil


#path = '/Users/karensommer/github/CS521_InformationStructuresWithPython/ksommer@bu_edu_hw_11/hw_11_2.txt'
path = 'hw_11_2.txt'
#target= '/Users/karensommer/github/CS521_InformationStructuresWithPython/ksommer@bu_edu_hw_11/target_11_2.txt'
target='target_11_2.txt'

if target.rfind('/')!=-1:
    target_folder=(target[:target.rfind('/')])
    # if target folder exists
    isExist_trg = os.path.exists(target_folder)
else:
    #assign the true by default because is going to store it in the root folder
    isExist_trg=True

# check if source path exists
isExist_src = os.path.exists(path)
#get extension of dource path
extension = os.path.splitext(path)[1]
if extension=='.txt' and isExist_src and isExist_trg:
    # check if the file exists
    isExist_file_target = os.path.exists(target)
    #print(isExist_file_target)
    if isExist_file_target:
        option=input('Do you want to overwrite the file y/n ?')
        if option.lower()=='y':
            #Make the copy
            shutil.copyfile(path, target)
            print('File copied!')
        else:
            print('File not copied')
    else:
        #Make the copy
        shutil.copyfile(path, target)
else:
    print('Invalid extension or src file not found or dest path not found')
