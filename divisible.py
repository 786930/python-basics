# Program name: divisible.py
# Your Name: Aerin Schmall
# Python Version: 3.7.8
# Date Started - Date Finished: 9/6/2020 - 9/6/2020
# Description: function that returns True if a number is evenly divisible by another

def isdivisible(n, m):
      if n % m == 0:
            return True
      else:
            return False
n = 4
m = 2      
print('%i is evenly divisible by %i:' %(n,m), isdivisible(n, m))
n = 5
m = 2      
print('%i is evenly divisible by %i:' %(n,m), isdivisible(n, m))
n = 6
m = 3      
print('%i is evenly divisible by %i:' %(n,m), isdivisible(n, m))

'''
============= RESTART: C:\\Users\\aerin\\Documents\\Python\\divisible.py ============
4 is evenly divisible by 2: True
5 is evenly divisible by 2: False
6 is evenly divisible by 3: True
'''
