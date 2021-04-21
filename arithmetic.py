# Program name: arithmetic.py
# Your Name: Aerin Schmall
# Python Version: 3.7.8
# Date Started - Date Finished: 9/1/2020 - 9/1/2020
# Description: creates a learning envo for a child ot learn addition subtraction multiplication
from random import randint

def add():
      while True:
            ad1 = randint(0,9)
            ad2 = randint(0,9)
            while True:
                  sumA = ad1+ad2
                  sumI = int(input('what is %i+%i equal to?: ' %(ad1,ad2)))
                  if sumI != sumA:
                        print('That is incorrect, ', end='')
                        continue
                  else:
                        break
            while True:
                  con = input('Correct! Would you like to try again? (y for yes, n for no): ')
                  if con != 'y' and con != 'n':
                        print('not a valid answer')
                        continue
                  else:
                        break
            if con == 'y':
                  continue
            else:
                  break

def sub():
      while True:
            ad1 = randint(0,9)
            ad2 = randint(0,9)
            while True:
                  sumA = ad1-ad2
                  sumI = int(input('what is %i-%i equal to?: ' %(ad1,ad2)))
                  if sumI != sumA:
                        print('That is incorrect, ', end='')
                        continue
                  else:
                        break
            while True:
                  con = input('Correct! Would you like to try again? (y for yes, n for no): ')
                  if con != 'y' and con != 'n':
                        print('not a valid answer')
                        continue
                  else:
                        break
            if con == 'y':
                  continue
            else:
                  break

def mult():
      while True:
            ad1 = randint(0,9)
            ad2 = randint(0,9)
            while True:
                  sumA = ad1*ad2
                  sumI = int(input('what is %i*%i equal to?: ' %(ad1,ad2)))
                  if sumI != sumA:
                        print('That is incorrect, ', end='')
                        continue
                  else:
                        break
            while True:
                  con = input('Correct! Would you like to try again? (y for yes, n for no): ')
                  if con != 'y' and con != 'n':
                        print('not a valid answer')
                        continue
                  else:
                        break
            if con == 'y':
                  continue
            else:
                  break
while True:
      choice = int(input('Would you like to add(1), subtract (2) or multiply(3): '))
      if choice not in range(1,4):
            print('not a valid choice')
            continue
      elif choice == 1:
            add()
      elif choice == 2:
            sub()
      else:
            mult()
      while True:
            choice = input('Would you do something else? (y/n): ')
            if choice != 'y' and choice != 'n':
                  print('not a valid choice')
                  continue
            else:
                  break
      if choice == 'y':
            continue
      else:
            print('Thank you for playing!')
            break


'''
============ RESTART: C:\\Users\\aerin\\Documents\\Python\\arithmetic.py ============
Would you like to add(1), subtract (2) or multiply(3): 1
what is 3+7 equal to?: 10
Correct! Would you like to try again? (y for yes, n for no): n
Would you do something else? (y/n): y
Would you like to add(1), subtract (2) or multiply(3): 2
what is 8-9 equal to?: -1
Correct! Would you like to try again? (y for yes, n for no): n
Would you do something else? (y/n): y
Would you like to add(1), subtract (2) or multiply(3): 3
what is 2*1 equal to?: 3
That is incorrect, what is 2*1 equal to?: 2
Correct! Would you like to try again? (y for yes, n for no): n
Would you do something else? (y/n): n
Thank you for playing!
'''
