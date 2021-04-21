# Program name: debug.py
# Your Name: Aerin Schmall
# Python Version: 3.7.8
# Date Started - Date Finished: 9/15/2020 - 9/15/2020
# Description: the program runs as intended in the bottom comment

num = int(input("Please enter a number: "))

def  isEven(num): # should have a parameter
  if  num % 2 == 0:
     return True
  elif num % 2 != 0:
     return False

def  main(): # needs to be called first
   print("The number %i is even: %s" %(num, isEven(num)))

main()
'''
============= RESTART: C:\\Users\\aerin\\Documents\\Python\\debug.py ==============
Please enter a number: 5
The number 5 is even: False
'''
