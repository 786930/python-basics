# Program name: random calculations.py
# Your Name: Aerin Schmall
# Python Version: 3.7.8
# Date Started - Date Finished: 9/6/2020 - 9/6/2020
# Description: generates a random amount of random numbers and calculates various things on them

from random import randint as rad

X = rad(10,15)
smol = rad(20,50)
big = smol
Sum = smol
print(f'Generating {X} random numbers (11 is a random number between 10 to 15):')
print(smol, end='')
for i in range(X-1):
      num = rad(20,50)
      print(',', num, end='')
      if num < smol:
            smol = num
      elif num > big:
            big = num
      Sum += num
print()
print('smalest: ', smol)
print('largest: ', big)      
print('sum: ', Sum)
print('average: %.1f' %(Sum/X))

'''
======== RESTART: C:\\Users\\aerin\\Documents\\Python\\random calculations.py =======
Generating 14 random numbers (11 is a random number between 10 to 15):
27, 28, 44, 40, 28, 43, 23, 36, 45, 22, 22, 21, 41, 45
smalest:  21
largest:  45
sum:  465
average: 33.2
'''
