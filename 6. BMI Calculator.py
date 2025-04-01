# -*- coding: utf-8 -*-
"""
Created on Sat Mar  1 20:45:30 2025

@author: Shariq
"""

weight = int(input("Enter your weight in Kg:"))

height = float(input('Enter your weight in Meters: '))

BMI = weight / (height**2)

print(BMI)

if BMI > 0:
    if BMI < 18.5:
        print ('You are Underweight!')
    elif (BMI > 18.5) and (BMI <= 24.9):
        print ('You are Normal weight!')
    elif (BMI > 25) and (BMI <= 29.9):
        print ('You are Overweight weight!')
    elif (BMI > 30) and (BMI <= 34.9):
        print ('You are Obese!')
    elif (BMI > 35) and (BMI <= 39.9):
        print ('You are Severly Obese!')
else:
    ("Enter valid details")


