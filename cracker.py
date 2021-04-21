# Program name: 
# Your Name: Aerin Schmall
# Python Version: 3.7.8
# Date Started - Date Finished: //2020 - //2020
# Description:
import zipfile as z

alp = 'abcdefghijklmnopqrstuvwxyz'

combo = []

for n in range(4):
      a = [i for i in alp]
      for x in range(n):
            a = [y+i for i in alp for y in a]
      combo = combo + a
zed = z.ZipFile('secret.zip')

t = 0
for p in combo:
      try:
            t+=1
            zed.setpassword(p.encode('ascii'))
            zed.extract('secret.txt')
            print(f'passcode: {p}   {t} tries')
      except:
            pass
'''
============= RESTART: C:\\Users\\aerin\\Documents\\Python\\
'''
