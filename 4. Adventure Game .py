# -*- coding: utf-8 -*-
"""
Created on Thu Jan  9 10:10:07 2025

@author: Shariq
"""

"""
This is a choose your own adventure game, like a pick your own story senario (childrens book
eg if you want to go right turn to pg 6). Different paths based on different decision.


Game is mainly about nested loops
"""

import random 

name = input("type your name: ")
print('Welcome', name, "to this adventure!")

answer = input(
    "you are on a dirt road you choose to can go left or right").lower()

# left
if answer == "left":
    answer = input(
        "you are now heading towards the lake would you like to swim or walk away").lower()
        
    if answer == "swim":
        print(" you died")
    elif answer == "walk":
        print("you walked away")
    else:
        print("answer invalid")
    
elif answer == "right":
    print()
    
    if answer == "swim":
        print(" you died")
    elif answer == "walk":
        print("you walked away")
    else:
        print("answer invalid")
else:
    print()