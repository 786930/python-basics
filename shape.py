# Program name: shape.py
# Your Name: Aerin Schmall
# Python Version: 3.7.8
# Date Started - Date Finished: 9/15/2020 - 9/15/2020
# Description: sees if four side lengths and angles create which quadrilateral 

sides = []
angles = []


def Values():
      global sides, angles
      print('''please choose sides and angles with their positin in mind:

angle 1 -- side 1 -- angle 2
  |                     |
  |                     |
side 4                side 2
  |                     |
  |                     |
angle 4 -- side 3 -- angle 3''')
      while True:
            sides = []
            print()
            print('====please enter sides')
            for i in range(4):
                  while True:
                        temp = round(float(input(f'Please enter side {i+1}: ')), 1)
                        if temp <= 0:
                              print('value must be greater than 0')
                              continue
                        elif temp > 0:
                              sides.append(temp)
                              break
            while True:
                  angles = []
                  print()
                  print('====please enter angles in degrees')
                  for i in range(4):
                        while True:
                              temp = round(float(input(f'Please enter angle {i+1}: ')), 0)
                              if temp <= 0:
                                    print('value must be greater than 0')
                              elif temp > 0:
                                    angles.append(temp)
                                    break
                  if angles[0]+angles[1]+angles[2]+angles[3] != 360:
                        print('Error: sum of all angles must be 360')
                        continue
                  elif angles[0]+angles[1]+angles[2]+angles[3] == 360:
                        break
            while True:
                  print()
                  print('side lengths: ', sides)
                  print('angles: ', angles)
                  temp = input('continue with these side lengths and angles? (y/n): ')
                  if temp != 'y' and temp != 'n':
                        print('please choose y or n')
                        continue
                  break
            if temp == 'y':
                  break
            if temp == 'n':
                  continue
      shape()
def shape():
      global sides, angles
      if angles[0] == angles[2] and angles[1] == angles[3] and angles[1] != angles[2]:
            if sides[0] == sides[1] and sides[2] == sides[3] and sides[1] == sides[2]:
                  print('=======================')
                  print('This is a RHOMBUS! ')
      elif angles[0] == angles[1] and angles[2] == angles[3] and angles[1] == angles[2]:
            if sides[0] == sides[1] and sides[2] == sides[3] and sides[1] == sides[2]:
                  print('=======================')
                  print('This is a SQUARE! ')
            elif sides[0] == sides[2] and sides[1] == sides[3]:
                  print('=======================')
                  print('This is a RECTANGLE! ')
      else:
            print('this is not a quadrilateral')
      while True:
            print()
            temp = input('Try another shape? (y/n): ')
            if temp != 'y' and temp != 'n':
                  print('please choose y or n')
                  continue
            if temp == 'y':
                  Values()
                  break
            if temp == 'n':
                  break
Values()

'''
============= RESTART: C:\\Users\\aerin\\Documents\\Python\\shape.py ==============
please choose sides and angles with their positin in mind:

angle 1 -- side 1 -- angle 2
  |                     |
  |                     |
side 4                side 2
  |                     |
  |                     |
angle 4 -- side 3 -- angle 3

====please enter sides
Please enter side 1: -1
value must be greater than 0
Please enter side 1: 1
Please enter side 2: 1
Please enter side 3: -1
value must be greater than 0
Please enter side 3: 1
Please enter side 4: 1

====please enter angles in degrees
Please enter angle 1: -1
value must be greater than 0
Please enter angle 1: 90
Please enter angle 2: 90
Please enter angle 3: -1
value must be greater than 0
Please enter angle 3: 90
Please enter angle 4: 90

side lengths:  [1.0, 1.0, 1.0, 1.0]
angles:  [90.0, 90.0, 90.0, 90.0]
continue with these side lengths and angles? (y/n): y
=======================
This is a SQUARE! 

Try another shape? (y/n): y
please choose sides and angles with their positin in mind:

angle 1 -- side 1 -- angle 2
  |                     |
  |                     |
side 4                side 2
  |                     |
  |                     |
angle 4 -- side 3 -- angle 3

====please enter sides
Please enter side 1: 1
Please enter side 2: 1
Please enter side 3: 1
Please enter side 4: 1

====please enter angles in degrees
Please enter angle 1: 120
Please enter angle 2: 60
Please enter angle 3: 120
Please enter angle 4: 40
Error: sum of all angles must be 360

====please enter angles in degrees
Please enter angle 1: 120
Please enter angle 2: 60
Please enter angle 3: 120
Please enter angle 4: 60

side lengths:  [1.0, 1.0, 1.0, 1.0]
angles:  [120.0, 60.0, 120.0, 60.0]
continue with these side lengths and angles? (y/n): n

====please enter sides
Please enter side 1: 1
Please enter side 2: 1
Please enter side 3: 1
Please enter side 4: 1

====please enter angles in degrees
Please enter angle 1: 120
Please enter angle 2: 60
Please enter angle 3: 120
Please enter angle 4: 60

side lengths:  [1.0, 1.0, 1.0, 1.0]
angles:  [120.0, 60.0, 120.0, 60.0]
continue with these side lengths and angles? (y/n): y
=======================
This is a RHOMBUS! 

Try another shape? (y/n): y
please choose sides and angles with their positin in mind:

angle 1 -- side 1 -- angle 2
  |                     |
  |                     |
side 4                side 2
  |                     |
  |                     |
angle 4 -- side 3 -- angle 3

====please enter sides
Please enter side 1: 10
Please enter side 2: 20
Please enter side 3: 10
Please enter side 4: 20

====please enter angles in degrees
Please enter angle 1: 90
Please enter angle 2: 90
Please enter angle 3: 90
Please enter angle 4: 90

side lengths:  [10.0, 20.0, 10.0, 20.0]
angles:  [90.0, 90.0, 90.0, 90.0]
continue with these side lengths and angles? (y/n): y
=======================
This is a RECTANGLE! 

Try another shape? (y/n): n
'''
