# Program name: input.py
# Your Name: Aerin Schmall
# Python Version: 3.7
# Date Started - Date Finished: 8/24/2020 - 8/24/2020
# Description: takes various inputs as variables and prints them to the shell

name = input("please enter your name: ") #this is a string
weightLbs = float(input("please enter your weight in Lbs: ")) # a float
age = int(input("please enter your age (whole number): ")) #and integer
weightKg = weightLbs*0.453592
title = "human"

print("hello ", title, name, "your weight is:")
print(weightLbs, "Lbs")
print("which equals = %.2f" %weightKg, end=' ')
print("kilograms")

'''
=============== RESTART: C:\\Users\\aerin\\Documents\\Python\\input.py ==============
please enter your name: aerin
please enter your weight in Lbs: 126
please enter your age (whole number): 14
hello  human aerin your weight is:
126.0 Lbs
which equals = 57.15 kilograms
'''
