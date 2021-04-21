# Program name: sumAverage.py
# Your Name: Aerin Schmall
# Python Version: 3.7.8
# Date Started - Date Finished: 9/2/2020 - 9/2/2020
# Description: takes a user designated amount of numbers and finds their doubles, sum, minimum and maximum


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
      print('your numbers are ', nums)
      sumNeg = nums[0]
      sumPos = nums[0]
      for i in nums:
            sumAll += i
            if i < sumNeg:
                  sumNeg = i
            elif i > sumPos:
                  sumPos = i
      print('their sum is %i' %sumAll)
      print('their average is %i/%i = %.1f' %(sumAll, length, sumAll/length))
      print('the minimum is %i' %sumNeg)
      print('the maximum is %i' %sumPos)
      for i in nums:
            double.append(i*2)
      print('the double of your numbers is:', double)

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
============= RESTART: C:\\Users\\aerin\\Documents\\Python\\sumAverage.py =========
enter how many numbers you want to add: 5
please input any 5 numbers (either positive or negative)
#1: 2
#2: 3
#3: -1
#4: 7
#5: -4
your numbers are  [2, 3, -1, 7, -4]
their sum is 7
their average is 7/5 = 1.4
the minimum is -4
the maximum is 7
the double of your numbers is: [4, 6, -2, 14, -8]
add new numbers? (y/n): n
'''
