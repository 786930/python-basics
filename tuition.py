# Program name: tuition.py
# Your Name: Aerin Schmall
# Python Version: 3.7.8
# Date Started - Date Finished: 8/31/2020 - 8/31/2020
# Description: outputs a table of college tuition over 10 years

year = 1
cost = 10000
while year < 10:
      print('year   %i     ' %year, int(cost))
      year += 1
      cost += cost*.05
print('year  %i     ' %year, int(cost))

'''
============== RESTART: C:\\Users\\aerin\\Documents\\Python\\tuition.py =============
year   1      10000
year   2      10500
year   3      11025
year   4      11576
year   5      12155
year   6      12762
year   7      13400
year   8      14071
year   9      14774
year  10      15513
'''
