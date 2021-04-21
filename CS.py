# Program name: CS.py
# Your Name: Aerin Schmall
# Python Version: 3.7
# Date Started - Date Finished: 8/24/2020 - 8/24/2020
# Description: prints out "CS!" in large block letters inside a border of *** 
# followed by two blank lines then the message "Computer Science is Cool Stuf" 
c = ['       C C C', '     C       C', '    C', '   C',
     '   C', '   C', '    C', '     C       C', '       C C C',]
s = ['     S S S\n','  S     S\n','          S\n','           S\n',
     '             S S S\n','                  S\n','          S       S\n',
     '  S     S\n','     S S S\n\n',]

for i in range(50):
      print('*', end='')

print('\n\n')
for i in range(len(c)):
      print(c[i], "     ", s[i])
for i in range(50):
      print('*', end='')
print('')
print("     Computer Science is Cool Stuf")
'''
================ RESTART: C:\\Users\\aerin\\Documents\\Python\\CS.py ================
**************************************************


       C C C            S S S

     C       C         S     S

    C                 S

   C                  S

   C                    S S S

   C                         S

    C                 S       S

     C       C         S     S

       C C C            S S S


**************************************************
     Computer Science is Cool Stuf
'''
