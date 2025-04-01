# -*- coding: utf-8 -*-
"""
Created on Tue Jan  7 16:06:05 2025
Shariq
"""

"""
The purpose of this quiz game is we want to ask the users the right answers to 
certain questions and  give them points. By the end we will print the number of
correct answers by each person.

"""

print("Welcome to my quiz !")

playing = input("Do you want to play? (Yes/No): ")

# checking if the player wants to play

if playing.lower() != "yes":     # adding .lower() will make the answer lowercase in case if someone types Yes or YEs 
    quit()                       # can terminate in between program with quit()

print("OK lets play")

score = 0


# Question 1 

qna1 = input("Who made this program?: ")

if qna1 == "shariq":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

 
# Question 2 

qna2 = input("Who lives in a pineapple under the sea?: ")

if qna2 == "sponge bob":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")


# Question 3

qna3 = input("2 + 3?: ")

if qna3 == "5":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")
 
    
# Score

print(" you got " + str(score) + " questions correct" )


# we made it in to a string because word + number doesnt make sence

"""
You learned

word + number doesnt make sence
.lower() <- adding .lower() will make the answer lowercase in case if someone types Yes or YEs 
score += 1
input()
quit() <- can terminate in between program with quit()

"""   