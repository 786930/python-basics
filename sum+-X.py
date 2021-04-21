# Program name: sum+-X.py
# Your Name: Aerin Schmall
# Python Version: 3.7.8
# Date Started - Date Finished: 8/30/2020 - 8/30/2020
# Description: takes a user designated amount of numbers and adds them all, all the negatives and all the positives


def cont():
      con = input('add new numbers? (y/n): ')
      
      return con

while True:
      sumAll=0
      nums = []
      double = []
      length = int(input('enter how many numbers you want to add: '))
                   
      print('please input any %i numbers (either positive or negative)' %length)
      for i in range(1,length+1):
            nums.append(int(input('#' + str(i) + ': ')))
      print()
      sumNeg = nums[0]
      sumPos = nums[0]
      for i in nums:
            sumAll += i
            if i <= 0:
                  sumNeg += i
            elif i >= 0:
                  sumPos += i
      print('their sum is %i' %sumAll)
      print('the sum of the negatives is %i' %sumNeg)
      print('the sum of the positives is %i' %sumPos)
      
      print()

      while True:
            con = cont()
            if con != 'y' and con != 'n':
                  print("not a valid answer")
                  
            else:
                  break
      if con == 'y':
            continue
      elif con == 'n':
            break
      
      
      

'''
============= RESTART: C:\\Users\\aerin\\Documents\\Python\\sum+-X.py =========
enter how many numbers you want to add: 5
please input any 5 numbers (either positive or negative)
#1: 1
#2: 3
#3: -2
#4: -7
#5: 5

their sum is 0
the sum of the negatives is -8
the sum of the positives is 10

add new numbers? (y/n): n
'''
