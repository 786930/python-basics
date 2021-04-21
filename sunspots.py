# Program name: sunspots.py
# Your Name: Aerin Schmall
# Python Version: 3.7.8
# Date Started - Date Finished: 9/11/2020 - 9/11/2020
# Description: takes data from sunspots.txt, calculates averages, and puts the averages 

aver = {}
file = open('sunspots.txt', 'r')
file2 = open('averages.txt', 'w')
line = file.read().split('\n')
line.pop(-1)
for i in line:
      values = i.split()
      tag = values[0]
      values.pop(0)
      ave = 0
      for j in values:
            ave += float(j)
      average = str(round(ave/len(values), 2))
      file2.write(tag + '    ' + average + '\n')
      
file.close()
file2.close()

'''
============= RESTART: C:\\Users\\aerin\\Documents\\Python\\sunspots.py =============
'''
