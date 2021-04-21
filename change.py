# Program name: change.py
# Your Name: Aerin Schmall
# Python Version: 3.7.8
# Date Started - Date Finished: 8/29/2020 - 8/29/2020
# Description: calculates coinage of a number of cents
q = 0
d = 0
n = 0
p = 0
while True:
      cent = int(input('please enter the number of cents from 0 to 100. '))
      if cent > 100 or cent < 0:
            print('outside of range')
      else:
            break
print('you have: ')
if cent == 0:
      print('no coins')
if cent >= 25:
      q = int(cent/25)
      print('%i quater(s) ' %q)
      cent = cent - q*25
if cent >= 10:
      d = int(cent/10)
      print('%i dime(s) ' %d)
      cent = cent - d*10
if cent >= 5:
      n = int(cent/5)
      print('%i nickel(s) ' %n)
      cent = cent - n*5
if cent >= 1:
      p = int(cent)
      print('%i pennie(s) ' %p)
      cent = cent - p
'''
============== RESTART: C:\\Users\\aerin\\Documents\\Python\\change.py ==============
please enter the number of cents from 0 to 100. 66
you have: 
2 quater(s) 
1 dime(s) 
1 nickel(s) 
1 pennie(s) 
===
please enter the number of cents from 0 to 100. 16
you have: 
1 dime(s) 
1 nickel(s) 
1 pennie(s) 
===
please enter the number of cents from 0 to 100. 6
you have: 
1 nickel(s) 
1 pennie(s) 
===
please enter the number of cents from 0 to 100. 4
you have: 
4 pennie(s) 
'''
