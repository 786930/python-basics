# Program name: isTriangle.py
# Your Name: Aerin Schmall
# Python Version: 3.7.8
# Date Started - Date Finished: 9/7/2020 - 9/7/2020
# Description: sees if three lengths can form a triangle

def triangle(a,b,c):
      if b > a+c:
            return False
      elif a > b+c:
            return False
      elif c > b+a:
            return False
      else:
            return True
print('is a triangle: ', triangle(int(input('side length 1: ')),int(input('side length 2: ')),int(input('side length 3: '))))

'''
============= RESTART: C:\\Users\\aerin\\Documents\\Python\\isTriangle.py ============
side length 1: 3
side length 2: 6
side length 3: 5
is a triangle:  True
'''
