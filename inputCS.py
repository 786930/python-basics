# Program name: inputCS
# Your Name: Aerin Schmall
# Python Version: 3.7.8
# Date Started - Date Finished: 8/25/2020 - 8/25/2020
# Description: prints the letter C made up of an inputed letter.
x = input("Enter a letter: ")
c = ['       %s %s %s' %(x,x,x), '     %s       %s' %(x,x),
     '    %s' %(x), '   %s' %(x), '   %s' %(x), '   %s' %(x),
     '    %s' %(x), '     %s       %s' %(x,x), '       %s %s %s' %(x,x,x),]
for i in range(50):
      print('*', end='')

print('\n\n')
for i in range(len(c)):
      print(c[i])
print("\n\n")
for i in range(50):
      print('*', end='')
print('')
print("     Computer Science is Cool Stuf")
'''
============== RESTART: C:\\Users\\aerin\\Documents\\Python\\inputCS.py =============
Enter a letter: D
**************************************************


       D D D
     D       D
    D
   D
   D
   D
    D
     D       D
       D D D



**************************************************
     Computer Science is Cool Stuf
'''
