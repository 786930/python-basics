# Program name: count letters.py
# Your Name: Aerin Schmall
# Python Version: 3.7.8
# Date Started - Date Finished: 9/6/2020 - 9/6/2020
# Description: takes a sentence and two letters, counts how many instances of the letter are in the sentence.
sent = input('Please enter a sentence: ').lower()
let1 = input('Please enter letter 1: ').lower()
let2 = input('Please enter letter 2: ').lower()
count = 0
for i in sent:
      
      if i == let1:
            count += 1
print(f'The letter {let1} occurs {count} time')
count = 0
for i in sent:
      if i == let2:
            count += 1
print(f'The letter {let2} occurs {count} time')

'''
=========== RESTART: C:\\Users\\aerin\\Documents\\Python\\count letters.py ==========
Please enter a sentence: supercalifragilisticexpialidocious
Please enter letter 1: a
Please enter letter 2: i
The letter a occurs 3 time
The letter i occurs 7 time
'''
