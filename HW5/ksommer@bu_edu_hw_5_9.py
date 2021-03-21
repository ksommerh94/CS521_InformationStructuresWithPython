'''

Karen Sommer

CS 521 Spring 2021

Assignment 5

Problem 9 pages 264-267

'''
#Write a function that takes as input an English sentence ( a string) and prints the total
#numbers of vowels and the total number of consonants in the sentence. The function
#returns nothing. Note that the sentece could have special characters such as dots, dashes
vowels=['a','e','i','o','u','A','E','I','O','U']

def count_vowel_consonants(str):
    count_vowles=0
    count_consonants=0
    for s in str:
        if s.isalpha():
            if s in vowels:
                count_vowles+=1
            else:
                count_consonants+=1
    print('Total number of vowels',count_vowles )
    print('Total number of consonants',count_consonants )



if __name__ == "__main__":
    print ('Enter a string')
    str = (input())
    count_vowel_consonants(str)
