'''
Project 1 - Number Categories - Spring 2023  
Author: Brunda Chagari 9065-61529

This program takes in a numeric value and returns wether the number is pronic
or perfect. The program does not take in values below zero and if entered returns
a prompt asking the user to re-enter a positive number. If -1 is enterd the
program quits.

I have neither given or received unauthorized assistance on this assignment.
Signed:  Brunda Chagari
'''

import math

def get_number():
    
    ''' Computes and returns wether a number is pronic or perfect based on
    the numbers value.
    Parameters:
    none
    Return: the number if it is > 0, also returns -1 of = to -1, also
    a prompt to enter a positive number if number is < 0'''
     
    sentence = "Enter a positive integer (or -1 to quit): "

    while True:
        number = int(input(sentence))
        
        if number == -1:
            return -1
        elif number < 0:
            sentence = "That number is not positive. Please reenter: "
        else:
            return number

def is_pronic(num):
    
    ''' Computes and returns wether a number is pronic based on
    the numbers value.
    Parameters:
    num- the number
    Return: True if pronic, False if not'''
     
    max_value = math.ceil(math.sqrt(num))
    
    for i in range(1, max_value):
        if i * (i+1) == num:
            return True
    return False

def is_perfect(num):
    
    '''Computes and returns wether a number is perfect based on
    the numbers value.
    Parameters:
    num- the number
    Return: True if perfect, False if not '''
     
    divisors_sum = 0
    
    for i in range(1, num):
        if num % i == 0:
            divisors_sum += i
            
    return divisors_sum == num

def main():
    
    '''combination of the other methods that computes and returns
    wether a number is pronic or perfect based on the numeric input
    the numbers value.
    Parameters: none
    Return: '' is pronic, if the number is pronic, is NOT pronic if the
    number is not pronic and likewise with perfect further the while
    loops prompts the user to keep entering numbers.'''
     
    while True:
        num = get_number()
    
        if num == -1:
            return
        
        if is_pronic(num):
            print("	is pronic")
        else:
            print("	is NOT pronic")
        
        if is_perfect(num):
            print("	is perfect \n")
        else:
            print("	is NOT perfect \n")
    


# Call main like this to keep Web-CAT happy:
if __name__ == '__main__':
    main()