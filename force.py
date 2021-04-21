# Program name: force.py
# Your Name: Aerin Schmall
# Python Version: 3.7.8
# Date Started - Date Finished: 12/3/2020 - 12/3/2020
# Description: brute forces finding a password and matching it to a hash
import hashlib as z

alp = ['Jane','Doe','Smith','02','13','1981','567','33','2013','831','228','5671','Kujo','Friendly']
combo = []

for n in range(3):
      a = [i for i in alp]
      for x in range(n):
            a = [y+i for i in alp for y in a]
      combo = combo + a
key = 'ae2e1fa899105c28184c0d0d11be8241'

t = 0
for p in combo:
      t+=1
      a = p.encode('utf-8')
      hsh = z.md5(a)
      dig = hsh.hexdigest()
      if dig == key:
            print('hash:', key)
            print(f'passcode: {p}   \n{t} tries')
            break


'''
============= RESTART: C:\\Users\\aerin\\Documents\\Python\\force.py ==============
hash: ae2e1fa899105c28184c0d0d11be8241
passcode: Kujo567Smith   
699 tries
'''
