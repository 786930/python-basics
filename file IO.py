# Program name: file IO.py
# Your Name: Aerin Schmall
# Python Version: 3.7.8
# Date Started - Date Finished: 9/10/2020 - 9/10/2020
# Description: reads and writes movie titles to two files

name = input('please enter a file name: ')
movies = [input(f'please enter movie title #{i}: ') for i in range(1,5)]
file = open(f'{name}', 'w')
for i in movies:
      file.write(i + '\n')
file.close()
file = open(f'{name}', 'r')
movie = file.read().splitlines()
print()
print(f'{name}.txt:')
print('\n'.join(movie)) # splitlines() only works with strings
file.close()
file = open('reverseOrder', 'w')
moviee = []
for i in range(4):
      file.write(movie[3-i] + '\n')
      moviee.append(movie[3-i])
print()
print('reverseOrder.txt:')
print('\n'.join(moviee))
file.close()
      

'''
============= RESTART: C:\\Users\\aerin\\Documents\\Python\\file IO.py =============
please enter a file name: movies
please enter movie title #1: nemo
please enter movie title #2: lion king
please enter movie title #3: hobbit
please enter movie title #4: bill and ted's excellent adventure

movies.txt:
nemo
lion king
hobbit
bill and ted's excellent adventure

reverseOrder.txt:
bill and ted's excellent adventure
hobbit
lion king
nemo
'''
