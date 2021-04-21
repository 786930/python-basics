# Program name: median.py
# Your Name: Aerin Schmall
# Python Version: 3.7.8
# Date Started - Date Finished: 9/10/2020 - 9/10/2020
# Description: makes a file of numbers, sorts those numbers and finds their median
from random import randint

def sort(l, t):
      if not t:
            for j in range(len(l)):
                  for i in range(len(l)-1):
                        if l[i] > l[i+1]:
                              temp = l[i]
                              l[i] = l[i+1]
                              l[i+1] = temp
      print(l)

file = open('numbers', 'w')
for i in range(randint(50,55)):
      file.write(str(randint(0,100)) + ',')
file.close()

file = open('numbers', 'r')
movies = file.read().split(',')
movies.remove('')

for i in range(len(movies)):
      movies[i] = int(movies[i])
sort(movies, False)
file.close()

if len(movies) % 2 == 0:
      temp = len(movies) // 2
      print('the median is', (movies[temp-1] + movies[temp]) // 2)
      
elif len(movies) % 2 != 0:
      temp = (len(movies)-1) // 2
      print('the median is', movies[temp])



'''
============= RESTART: C:\\Users\\aerin\\Documents\\Python\\median.py ==============
[2, 2, 4, 5, 9, 15, 16, 17, 17, 20, 25, 25, 26, 28, 29, 33, 34, 40, 40, 41, 44, 44, 49, 49, 50, 54, 55, 57, 59, 60, 61, 62, 63, 63, 64, 66, 67, 68, 69, 70, 72, 72, 73, 76, 77, 77, 78, 81, 86, 89, 90, 92, 98, 98]
the median is 56
'''
