# Program name: count letters.py
# Your Name: Aerin Schmall
# Python Version: 3.7.8
# Date Started - Date Finished: 9/6/2020 - 9/6/2020
# Description: takes a sentence and two letters, counts how many instances of the letter are in the sentence.
from random import randint as r
sent = []
count = 0
l = r(15,20)
for i in range(l):
      sent.append(r(2,5))

for i in sent:
      if i == 3:
            count += 1
print(f'generating a list of {l} numbers')
print(sent)
print(f'The number 3 occurs {count} times')

'''
=========== RESTART: C:\\Users\\aerin\\Documents\\Python\\count numbers.py ==========
generating a list of 17 numbers
[3, 5, 5, 4, 3, 2, 4, 2, 4, 5, 2, 3, 3, 3, 4, 4, 5]
The number 3 occurs 5 times
'''
