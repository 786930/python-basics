# Program name: voting.py
# Your Name: Aerin Schmall
# Python Version: 3.7.8
# Date Started - Date Finished: 8/29/2020 - 8/29/2020
# Description: checks if a user can vote

while True:
      age = int(input('please enter your age: '))
      reg = input('are you registered? (y/n): ')
      cit = input('are you a citizen? (y/n): ')
      if reg != 'y' and reg != 'n' or cit != 'y' and cit != 'n':
            print('please enter "y" or "n"')
      else:
            break
      
if age >= 18 and cit == 'y' and reg == 'y':
      print('congrats! you can vote!')
else:
      print('sorry you cannot vote')
      if age < 18:
            print('- you must be over 18')
      if cit == 'n':
            print('- you must be a citizen')
      if reg == 'n':
            print('- you must be registered')
      
'''
============== RESTART: C:\\Users\\aerin\\Documents\\Python\\voting.py ==============
please enter your age: 18
are you registered? (y/n): y
are you a citizen? (y/n): y
congrats! you can vote!
>>> 
===
please enter your age: 17
are you registered? (y/n): y
are you a citizen? (y/n): y
sorry you cannot vote
- you must be over 18
>>> 
===
please enter your age: 19
are you registered? (y/n): n
are you a citizen? (y/n): y
sorry you cannot vote
- you must be registered
>>> 
===
please enter your age: 20
are you registered? (y/n): n
are you a citizen? (y/n): n
sorry you cannot vote
- you must be a citizen
- you must be registered
'''
