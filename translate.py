# Program name: translate.py
# Your Name: Aerin Schmall
# Python Version: 3.7.8
# Date Started - Date Finished: 12/8/2020 - //2020
# Description:

import gettext

print(_("original"))
print (_( "===+++===&&&---"))
print (_("Good morning"))
print ("Good night")

print(_("please enter 3 numbers"))
Sum = 0
for i in range(0,3,1):
	num = float ( input ( _( "Please enter number ") +str(i+1) +":") )
	Sum += num
	
print("The sum of the numbers you entered" + str(Sum))
'''
============= RESTART: C:\\Users\\aerin\\Documents\\Python\\
'''
