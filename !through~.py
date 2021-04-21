# Program name: !through~.py
# Your Name: 786930
# Python Version: 3.7.8
# Date Started - Date Finished: 9/1/2020 - 9/1/2020
# Description: prints a table of ASCII characters

for asciiV in range(94):
      if (asciiV) %10 == 0 and asciiV != 0: print() # not the best way to format, but wanted the least lines as possible
      print(chr(asciiV+33), end = ' ')

'''
============= RESTART: C:\\Users\\*\\Documents\\Python\\!through~.py ============
! " # $ % & ' ( ) * 
+ , - . / 0 1 2 3 4 
5 6 7 8 9 : ; < = > 
? @ A B C D E F G H 
I J K L M N O P Q R 
S T U V W X Y Z [ \ 
] ^ _ ` a b c d e f 
g h i j k l m n o p 
q r s t u v w x y z 
{ | } ~ 
'''
