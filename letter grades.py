# Program name: letter grades.py
# Your Name: Aerin Schmall
# Python Version: 3.7.8
# Date Started - Date Finished: 8/28/2020 - 8/28/2020
# Description: takes your grade and outputs message based on it

feet = 0
def height ():
      global feet
      feet = int(input("please enter your grade in percent: "))
      
      if (feet < 0) or (feet > 100):
            print("please input a number between 0 and 100")
            height()
      
height()


if (feet) >= 90:
      print('you have an "A"')
elif (feet) >= 80:
      print('you have a "B"')
elif (feet) >= 70:
      print('you have a "C"')
elif (feet) >= 60:
      print('you have a "D"')
else:
      print('you have an "F"')
      

'''
=========== RESTART: C:\\Users\\aerin\\Documents\\Python\\letter grades.py ==========
please enter your grade in percent: -5
please input a number between 0 and 100
please enter your grade in percent: 101
please input a number between 0 and 100
please enter your grade in percent: 70
you have a "C"
'''
