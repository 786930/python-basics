# Program name: Rock Paper Scissors.py
# Your Name: Aerin Schmall
# Python Version: 3.7.8
# Date Started - Date Finished: 8/28/2020 - 8/28/2020
# Description: play rock paper scissors
import random

options = ['R', 'P', 'S']
win = [['R', 'P'], ['P', 'R'], ['S', 'R'], ['R', 'S'], ['P', 'S'], ['S', 'P']]
feet = ''
pl2= options[random.randint(0,2)]
print("let's play rock, paper, scissors!")
def height ():
      global feet
      feet = input("please enter R, P, or S: ")
      
      if feet not in options:
            print("not a valid choice")
            height()
      
height()
print('player 2 chose %s' %pl2)
winner = [feet, pl2]

if winner not in win:
      print("it's a tie!")
elif win.index(winner) %2 != 0:
      print('you win!')

elif win.index(winner) %2 == 0:
      print('you lost...')

      

'''
======== RESTART: C:\\Users\\aerin\\Documents\\Python\\Rock Paper Scissors.py =======
let's play rock, paper, scissors!
please enter R, P, or S: f
not a valid choice
please enter R, P, or S: S
player 2 chose R
you lost...
'''
