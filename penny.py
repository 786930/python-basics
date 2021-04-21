# Program name: penny.py
# Your Name: Aerin Schmall
# Python Version: 3.7.8
# Date Started - Date Finished: 9/1/2020 - 9/1/2020
# Description: calculates the difference between $1 mil and a doubling penny over 30 days

pen = .01
for i in range(30):
      pen = pen*2
if pen < 1000000:
      print('you would lose $%.2f' %(1000000-pen))
else:
      print('you would gain $%.2f' %(pen-1000000))

'''
=============== RESTART: C:\\Users\\aerin\\Documents\\Python\\penny.py ==============
you would gain $9737418.24
'''
