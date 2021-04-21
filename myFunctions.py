# Program name: myFunctions.py
# Your Name: Aerin Schmall
# Python Version: 3.7.8
# Date Started - Date Finished: 9/11/2020 - 9/11/2020
# Description: various functions to be used in testFunctions.py

def Min(l):
      smol = l[0]
      for i in l:
            if i < smol:
                  smol = i
      return smol

def Max(l):
      smol = l[0]
      for i in l:
            if i > smol:
                  smol = i
      return smol

def Sum(l):
     Sum = 0
     for i in l:
           Sum += i
     return Sum

def Avg(l):
      Avg = Sum(l)/len(l)
      return round(Avg, 2)

def Abs(n):
      if n >= 0:
            return n
      else:
            return -n

def Find(k, l):
      if k in l:
            return True
      else:
            return False

def IsEven(n):
      if n % 2 == 0:
            return True
      else:
            return False

'''
============= RESTART: C:\\Users\\aerin\\Documents\\Python\\myFunctions.py
'''
