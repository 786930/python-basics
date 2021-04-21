# Program name: compute height.py
# Your Name: Aerin Schmall
# Python Version: 3.7.8
# Date Started - Date Finished: 8/25/2020 - 8/25/2020
# Description: takes your height and computes it as inches
feet = 0
inches = 0
print ("please enter your height")
def height ():
      global feet
      global inches
      feet = int(input("the number of feet: "))
      inches = int(input("the number of inches: "))
      if (feet < 0):
            print("please input a positive number")
            height()
      elif (inches < 0):
            print("please input a positive number")
            height()
height()


print("%i feet, %i inch(es) = " %(feet, inches), feet*12+inches )

'''
========== RESTART: C:\\Users\\aerin\\Documents\\Python\\compute height.py ==========
please enter your height
the number of feet: 5
the number of inches: 6
5 feet, 6 inch(es) =  66
'''
