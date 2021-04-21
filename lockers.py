# Program name: lockers.py
# Your Name: Aerin Schmall
# Python Version: 3.7.8
# Date Started - Date Finished: 9/10/2020 - 9/10/2020
# Description: checks if a locker is open

lockers = [False for _ in range(1000)]
for i in range(1,1001):
      for j in range(1,1001,i):
            if lockers[j-1] == True:
                  lockers[j-1] = False
            elif lockers[j-1] == False:
                  lockers[j-1] = True
count = 0
for i in range(1000):
      if lockers[i] == True:
            print(f'Locker Number {i} is open')
            count += 1
print(f'there are {count} lockers open')

'''
============= RESTART: C:\\Users\\aerin\\Documents\\Python\\lockers.py =============
Locker Number 1 is open
Locker Number 4 is open
Locker Number 9 is open
Locker Number 16 is open
Locker Number 25 is open
Locker Number 36 is open
Locker Number 49 is open
Locker Number 64 is open
Locker Number 81 is open
Locker Number 100 is open
Locker Number 121 is open
Locker Number 144 is open
Locker Number 169 is open
Locker Number 196 is open
Locker Number 225 is open
Locker Number 256 is open
Locker Number 289 is open
Locker Number 324 is open
Locker Number 361 is open
Locker Number 400 is open
Locker Number 441 is open
Locker Number 484 is open
Locker Number 529 is open
Locker Number 576 is open
Locker Number 625 is open
Locker Number 676 is open
Locker Number 729 is open
Locker Number 784 is open
Locker Number 841 is open
Locker Number 900 is open
Locker Number 961 is open
there are 31 lockers open
'''
