# Program name: functions     
# Your Name: Aerin Schmall
# Python Version: 3.7.8
# Date Started - Date Finished: 9/10/2020 - 9/10/2020
# Description: the definitions for the functions sum() , average(), min(), max()

def Sum(l):
      s = 0
      for i in l:
            s += i
      return s

def Average(l):
      s = 0
      for i in l:
            s += i
      return s/len(l)

def Min(l):
      m = l[0]
      for i in l:
            if i < m:
                  m = i
      return m

def Max(l):
      m = l[0]
      for i in l:
            if i > m:
                  m = i
      return m

def Main():
      l = [1,3,6,-1,-5]
      print('the list is', l)
      print('the sum is', Sum(l))
      print('the average is', Average(l))
      print('the minimum is', Min(l))
      print('the maximum is', Max(l))
Main()

'''
============= RESTART: C:\\Users\\aerin\\Documents\\Python\\functions.py ============
the list is [1, 3, 6, -1, -5]
the sum is 4
the average is 0.8
the minimum is -5
the maximum is 6
'''
