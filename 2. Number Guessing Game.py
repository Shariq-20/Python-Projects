# -*- coding: utf-8 -*-
"""
Created on Tue Jan  7 16:06:05 2025
Shariq
"""

"""
The purpose of this is trying to generate a random number and track how many times
it takes the use to guess this number

"""
import random

# to print a random number we use

r = random.randrange(1, 11)         # if you put 11 will generate up to 10 (using range fn with random)
print(r)

# or could use 

r = random.randrange(1, 11)         # with randint 11 will be printed for some reason
print(r)


#--------------- starting code

# identify a max range to guess from eg guess only in between 0 to 10

top_of_range = input("Type a number to set the guess range: ")     # remember if the user types some number here it will still be a string 

# need to make sure user types in a number

if top_of_range.isdigit():            # isdigit() checks if the input str is a number returns true or false
    top_of_range = int(top_of_range)  # if isdigit is true then the if statment will to make the value into int using int()
    
    # checking if the number is greater than 0
    if top_of_range <= 0:
        print('please type a number larger than 0 next time. ')
        quit()
# if they didnt type a number tell them 
else:
    print('please type a number next time ')
    quit()                                      # to terminate and restart
        

random_number = random.randrange(0, top_of_range)         
print(r)


# playing the guessing game -> tell the user to keep on trying 
guesses = 0

while True:
    guesses += 1
    user_guess = input("make a guess ")
    
    if user_guess.isdigit():            
        user_guess = int(user_guess)
        
    else:
        print('please type a number next time ')
        continue                # rather than ending go back to the top of loop
          
    if user_guess == random_number:
        print("you got it!")
        break                   # to avoid infinite loop
    else:
        if user_guess > random_number:
            print(" your guess is higher than the number")
        else:
            print(" your guess is lower than the number")
        
        
print ("you got it in" , guesses, "guesses" )  #when ever you use , automatically adds spaces


"""
You learned

# to print a random number we use
    r = random.randrange(1, 11)         # if you put 11 will generate up to 10 (using range fn with random)
    print(r)

# or could use 

    r = random.randrange(1, 11)         # with randint 11 will be printed for some reason
    print(r)


+  break() - in Python is used to terminate the loop or statement in which it is present.
If the break statement is present in the nested loop, then it terminates only those loops which contain the break statement. 

+  continue() - instead of terminating the loop, it forces to execute the next iteration of the loop. 
As the name suggests the continue statement forces the loop to continue or execute the next iteration.


"""  