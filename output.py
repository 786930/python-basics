# Program name: output.py
# Your Name: Aerin Schmall
# Python Version: 3.7.8
# Date Started - Date Finished: 8/24/2020 - 8/24/2020
# Description: program to print various variables to the shell

print('hello world') #single quote
print("hello world") #double quote
print("he\nllo") #\n insert new line (same as pressing enter)

# variables are names storage locations for numbers, strings, lists
#STRING is anything enclosed in quotes "hello world", that's a string
#NUMBER can be either a FLOAT (EX: 9.3) or an INTEGER (Ex: 9.0)
#LISTS are things like [1,2,3] or ["alex","stoykov"]
myName = "aerin" # declare/initialize sttring variable myName
Weight = 126.7 #declare/initialize float variable Weight
Age = 14 #declare/initialize int variable Age
Grades = [100,80,95]
nameZ = ["Aerin","Schmall"]

print("Hello ", myName)
print("your wight is ", Weight, "and your age is ", Age)
print("your wight is %.2f and your age is %i" %(Weight,Age))
print ("Lists: grades = ", Grades, "nameZ = ", nameZ)
print ("this is how you print", end=' ')
print("on the same line")

"""
============== RESTART: C:\\Users\\aerin\\Documents\\Python\\output.py ==============
hello world
hello world
he
llo
Hello  aerin
your wight is  126.7 and your age is  14
your wight is 126.70 and your age is 14
Lists: grades =  [100, 80, 95] nameZ =  ['Aerin', 'Schmall']
this is how you print on the same line
"""
# the first line had to have double \ even though thats not what is outputed
# otherwise the code throws a unicodeescape error
