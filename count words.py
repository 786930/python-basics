# Program name: count words.py
# Your Name: Aerin Schmall
# Python Version: 3.7.8
# Date Started - Date Finished: 9/9/2020 - 9/9/2020
# Description: takes a sentence, counts the words, tells the last word, sees how many times a word appears in it

words = input('enter a sentence: ').split()
print(f'there are {len(words)} words in your sentence')
print(f'the last word is {words[-1]}')
word = input('please enter a word: ')
count = 0
for i in words:
      if i == word:
            count += 1
print(f'The word "{word}" appears {count} times')
'''
============= RESTART: C:\\Users\\aerin\\Documents\\Python\\count words.py ===========
enter a sentence: the pigs went to the store to pick up the bread
there are 11 words in your sentence
the last word is bread
please enter a word: the
The word "the" appears 3 times
'''
