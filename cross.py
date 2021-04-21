# Program name: cross.py
# Your Name: Aerin Schmall
# Python Version: 3.7.8
# Date Started - Date Finished: 9/2/2020 - 9/3/2020
# Description: prints lines of + increasing by 1 until there is as many as was designated

def stars(cross):
      for i in range(cross):
            for y in range(cross-i):
                  print(end = ' ')
            for x in range(i+1):
                  print('+', end=' ')
            print()
cross = int(input('please enter a number: '))
stars(cross)
'''
============= RESTART: C:\\Users\\aerin\\Documents\\Python\\cross.py ==============
please enter a number: 10
          + 
         + + 
        + + + 
       + + + + 
      + + + + + 
     + + + + + + 
    + + + + + + + 
   + + + + + + + + 
  + + + + + + + + + 
 + + + + + + + + + + 
'''
