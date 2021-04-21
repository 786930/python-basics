# Program name: testFunctions.py
# Your Name: Aerin Schmall
# Python Version: 3.7.8
# Date Started - Date Finished: 9/11/2020 - 9/11/2020
# Description: import a file previously made and test the functions of that file
import myFunctions as m

test = [2,3,6,-1,-5,9]

print(test, '\n',
      'Min:', m.Min(test), '\n',
      'Max:', m.Max(test),'\n',
      'Average:', m.Avg(test),'\n',
      'Sum:', m.Sum(test),'\n',
      'Absolute value of -4:', m.Abs(-4),'\n',
      'Find 3 in list:', m.Find(3, test),'\n',
      '4 Is Even:', m.IsEven(4))


'''
============= RESTART: C:\\Users\\aerin\\Documents\\Python\\testFunctions.py ==========
[2, 3, 6, -1, -5, 9] 
 Min: -5 
 Max: 9 
 Average: 2.33 
 Sum: 14 
 Absolute value of -4: 4 
 Find 3 in list: True 
 4 Is Even: True
'''
