# Program name: protein shake.py
# Your Name: Aerin Schmall
# Python Version: 3.7.8
# Date Started - Date Finished: 12/3/2020 - 12/3/2020
# Description: gives the protein weight for a string of amino acids
f = open("aa.txt", "r")
lines = f.read()
lines = lines.split('\n')
weights = {}
for i in lines:
      j = i.split('   ')
      weights[j[0]] = float(j[1])
while True:
      a=False
      string = input('please enter an amino acid string: ').upper()
      for i in string:
            if i not in weights.keys():
                  print('invalid character:', i)
                  a=False
                  break
            else:
                  a=True
      if a:
            break
      continue

sm = 0
for i in string:
      sm += weights[i]

print('total weight:', round(sm, 3))
f.close()
'''
============= RESTART: C:\\Users\\aerin\\Documents\\Python\\protein shakes.py ==========
please enter an amino acid string: bbc
invalid character: B
please enter an amino acid string: ddefgh
total weight: 700.245
'''
