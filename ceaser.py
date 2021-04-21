# Program name: ceaser.py
# Your Name: Aerin Schmall
# Python Version: 3.7.8
# Date Started - Date Finished: 12/1/2020 - 12/1/2020
# Description: ceasar cypher

alp = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
print('alphabet = ', alp)

chift = 3
print('shift =', chift, 'letters')

enc = ''
encrypt = {' ':' '}
dec = {' ':' '}

def ency(ch):
      global enc, encrypt, dec, alp
      enc = alp[ch:] + alp[:ch]
      print('encrypted = ', enc)

      for i in range(len(alp)):
            encrypt[alp[i]] = enc[i]
            dec[enc[i]] = alp[i]
ency(chift)

original = 'hello world'
original = original.upper()
encrypted = ''
for i in original:
      encrypted += encrypt[i]
      
print('original sentence: ', original)
print('encrypted sentence: ', encrypted)
print('... decyphered: ', end='')
for i in range(len(encrypted)):
      print(dec[encrypted[i]], end='')

ency(13)
print('CLGUBA VF TERNG... decyphered: ', end='')
for i in 'CLGUBA VF TERNG':
      print(dec[i], end='')
'''
============= RESTART: C:\\Users\\aerin\\Documents\\Python\\ceaser.py ==============
alphabet =  ABCDEFGHIJKLMNOPQRSTUVWXYZ
shift = 3 letters
encrypted =  DEFGHIJKLMNOPQRSTUVWXYZABC
original sentence:  HELLO WORLD
encrypted sentence:  KHOOR ZRUOG
... decyphered: HELLO WORLDencrypted =  NOPQRSTUVWXYZABCDEFGHIJKLM
CLGUBA VF TERNG... decyphered: PYTHON IS GREAT
'''
