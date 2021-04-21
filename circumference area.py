# Program name: circumference area.py
# Your Name: Aerin Schmall
# Python Version: 3.7.8
# Date Started - Date Finished: 8/26/2020 - 8/26/2020
# Description: takes a radius and outputs circumference and area

rad = 0
print ("circumference and area of a circle")
def height ():
      global rad
      rad = int(input("What is the radius (in inches) of the circle you want to draw? "))
      if (rad < 0):
            print("please input a positive number")
            height()
height()
circ = 3.1415*rad*2
area = 3.1415*rad*rad

print("A circle with radius %i inches has" %(rad))
print("circumference:   %.1f inches" %(circ))
print("area:   %.1f sq. inches" %(area))

'''
======== RESTART: C:\\Users\\aerin\\Documents\\Python\\circumference area.py ========
circumference and area of a circle
What is the radius (in inches) of the circle you want to draw? 4
A circle with radius 4 inches has
circumference:   25.1 inches
area:   50.3 sq. inches
'''
