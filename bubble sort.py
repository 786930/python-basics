# Program name: bubble sort.py
# Your Name: Aerin Schmall
# Python Version: 3.7.8
# Date Started - Date Finished: 9/10/2020 - 9/10/2020
# Description: sorts a list from least to greatest or revers depending on a bool

def sort(l, t):
      if t:
            for j in range(len(l)):
                  for i in range(len(l)-1):
                        if l[i] < l[i+1]:
                              temp = l[i]
                              l[i] = l[i+1]
                              l[i+1] = temp
      elif not t:
            for j in range(len(l)):
                  for i in range(len(l)-1):
                        if l[i] > l[i+1]:
                              temp = l[i]
                              l[i] = l[i+1]
                              l[i+1] = temp
      print(l)
sort([5, 2, 8, 0], False)

'''
============= RESTART: C:\\Users\\aerin\\Documents\\Python\\bubble sort.py ===========
[0, 2, 5, 8]
'''
