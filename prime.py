# Program name: prime.py
# Your Name: Aerin Schmall
# Python Version: 3.7.8
# Date Started - Date Finished: 9/10/2020 - 9/10/2020
# Description: calculates and prints all prime numbers between 3 and 100

for i in range(3,100):
      prime = True
      for j in range(2,i-1):
            if i%j == 0:
                  prime = False
      if prime:
            print(i)
      

'''
============= RESTART: C:\\Users\\aerin\\Documents\\Python\\prime.py ==============
3
5
7
11
13
17
19
23
29
31
37
41
43
47
53
59
61
67
71
73
79
83
89
97
'''
