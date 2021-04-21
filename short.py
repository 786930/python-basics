# Program name: short.py 
# Your Name: Aerin Schmall
# Python Version: 3.7.8
# Date Started - Date Finished: 9/15/2020 - 9/15/2020
# Description: two functions that calculate speed and the median of 3 nums

def speed(distance, time):
      speed = distance/time
      return round(speed, 2)
print(speed(40.65, 3.154))

def median(x,y,z):
      l = [x,y,z]
      for j in range(len(l)):
                  for i in range(len(l)-1):
                        if l[i] > l[i+1]:
                              temp = l[i]
                              l[i] = l[i+1]
                              l[i+1] = temp
      return l[1]
print(median(5,1,2))
'''
============= RESTART: C:\\Users\\aerin\\Documents\\Python\\short.py ==============
12.89
2
'''
