# Program name: longest word.py
# Your Name: Aerin Schmall
# Python Version: 3.7.8
# Date Started - Date Finished: 9/9/2020 - 9/9/2020
# Description: takes a list and returns the longest word in it

words = input('enter a sentence: ').split()
short = words[0]
for i in words:
      if len(i) > len(short):
            short = i
print(f'longest word is {short}')
print(f'it is {len(short)} characters long')

'''
============= RESTART: C:\\Users\\aerin\\Documents\\Python\\longest word.py ===========
enter a sentence: I am a walrus
longest word is walrus
it is 6 characters long
'''
