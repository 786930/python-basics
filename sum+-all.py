# Program name: sum+-all.py
# Your Name: Aerin Schmall
# Python Version: 3.7.8
# Date Started - Date Finished: 8/30/2020 - 8/30/2020
# Description: takes 4 numbers and adds them all, adds all the negatives and all the positives

sumAll=0
sumNeg=0
sumPos=0
nums = []

print('please input any 4 numbers (either positive or negative)')
for i in range(1,5):
      nums.append(int(input('#' + str(i) + ': ')))
print('your numbers are ', nums)
for i in nums:
      sumAll += i
      if i <= 0:
            sumNeg += i
      elif i >= 0:
            sumPos += i
print('their sum is %i' %sumAll)
print('the sum of the negatives is %i' %sumNeg)
print('the sum of the positives is %i' %sumPos)

'''
============= RESTART: C:\\Users\\aerin\\Documents\\Python\\sum+-all.py =============
please input any 4 numbers (either positive or negative)
#1: 3
#2: 5
#3: -4
#4: -10
your numbers are  [3, 5, -4, -10]
their sum is -6
the sum of the negatives is -14
the sum of the positives is 8
'''
