# -*- coding: utf-8 -*-
"""
Created on Thu Jan  9 08:45:12 2025
@author: Shariq
"""

"""
Making a rock, paper and scissors game

"""
import random

user_wins= 0
computer_wins= 0

options = ["r", "p", "s"]

while True:
    # Identifying our input
    user_input = input("select R/P/S or Q to quit: ").lower()
    if user_input == "q":
        break   #to stop program if wanted
    
    # Need to make sure user types in a one of the options
    if user_input not in options:            # rather than using an if/else mix could use a list  
        continue    
    
    # Now to make a way for the cpu too play
    random_number = random.randint(0,2)      # rock:0, paper:1, scissors:2
    cpu = options[random_number]
    
    print("computer picked", cpu + ".")
    
    # Rules Check - rock, paper, scissor
    if user_input == 'r' and cpu =='s':
        print("You won!")
        user_wins += 1
    
    elif user_input == 'p' and cpu =='r':
        print("You won!")
        user_wins += 1
    
    elif user_input == 's' and cpu =='p':
        print("You won!")
        user_wins += 1
    
    else:
        print ("You lost!")
        computer_wins +=1
    
print("You won", user_wins , "times" )   
print("You lost", computer_wins , "times" )
print("Good Bye!")


"""
learnt

+ Remember continue reuses the loop

+ can use random and then a list to selet item from list

+ found a way to use (not in)

"""