# Program name: dice.py
# Your Name: Aerin Schmall
# Python Version: 3.7.8
# Date Started - Date Finished: 9/1/2020 - 9/1/2020
# Description: play dice against comp
from random import randint

def cont():
      con = input('roll again? (y/n):\n ')
      
      return con
print('Beat the computer!')
while True:
      d1=randint(1,6)
      d2=randint(1,6)
      sumd=d1+d2
      comp1 = randint(1,6)
      comp2 = randint(1,6)
      sumc = comp1+comp2
      print('You rolled a %i and a % i(total = %i)' %(d1,d2,sumd))
      
      while True:
            con = cont()
            if con != 'y' and con != 'n':
                  print("not a valid answer")
                  
            else:
                  break
      if con == 'y':
            print('rolling again...')
            continue
      elif con == 'n':
            print('The computer rolled a %i and a % i(total = %i)' %(comp1,comp2,sumc))
            if sumc == sumd:
                  print("it's a tie!")
            elif sumc < sumd:
                  print("you win!")
            elif sumc > sumd:
                  print("you lost...")
            break
      
      
      

'''
=============== RESTART: C:\\Users\\aerin\\Documents\\Python\\dice.py ===============
Beat the computer!
You rolled a 3 and a  3(total = 6)
roll again? (y/n):
 n
The computer rolled a 4 and a  4(total = 8)
you lost...
>>> 
===
Beat the computer!
You rolled a 1 and a  1(total = 2)
roll again? (y/n):
 y
rolling again...
You rolled a 6 and a  3(total = 9)
roll again? (y/n):
 y
rolling again...
You rolled a 5 and a  6(total = 11)
roll again? (y/n):
 n
The computer rolled a 4 and a  1(total = 5)
you win!
===
Beat the computer!
You rolled a 1 and a  1(total = 2)
roll again? (y/n):
 y
rolling again...
You rolled a 2 and a  2(total = 4)
roll again? (y/n):
 y
rolling again...
You rolled a 4 and a  5(total = 9)
roll again? (y/n):
 n
The computer rolled a 6 and a  4(total = 9)
it's a tie!
'''
