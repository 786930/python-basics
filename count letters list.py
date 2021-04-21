# Program name: count letters list.py
# Your Name: Aerin Schmall
# Python Version: 3.7.8
# Date Started - Date Finished: 9/6/2020 - 9/6/2020
# Description: counts the letter B in a list of random letters
from random import randint as r
sent = []
count = 0
l = r(50,75)
for i in range(l):
      sent.append(chr(r(65,70)))

for i in sent:
      if i == 'B':
            count += 1
print(f'generating a list of {l} letters')
print(sent)
print(f'The letter B occurs {count} times')

'''
=========== RESTART: C:\\Users\\aerin\\Documents\\Python\\count letters list.py ==========
generating a list of 58 letters
['C', 'A', 'F', 'F', 'F', 'F', 'C', 'F', 'A', 'D', 'F', 'C', 'F', 'F', 'E', 'C', 'A', 'D', 'B', 'C', 'F', 'A', 'B', 'D', 'C', 'E', 'F', 'E', 'B', 'F', 'B', 'E', 'A', 'D', 'C', 'B', 'F', 'E', 'E', 'F', 'B', 'D', 'B', 'A', 'F', 'E', 'E', 'D', 'D', 'C', 'C', 'E', 'E', 'A', 'B', 'B', 'F', 'C']
The letter B occurs 9 times
'''
