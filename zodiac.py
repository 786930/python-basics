# Program name: zodiac.py
# Your Name: Aerin Schmall
# Python Version: 3.7.8
# Date Started - Date Finished: 8/30/2020 - 8/30/2020
# Description: tells you your zodiac sign and compatabilities
zodiac = {1:{19:"You are Capricorn, part of the Earth group\ncompatible with Taurus, Virgo, Capricorn",
             20:"You are Aquarius, part of the Air group\ncompatible with Gemini, Libra, Aquarius"},
          2:{18:"You are Aquarius, part of the Air group\ncompatible with Gemini, Libra, Aquarius",
             19:"You are Pisces, part of the Water group\ncompatible with Cancer, Scorpio, Pisces"},
          3:{20:"You are Pisces, part of the Water group\ncompatible with Cancer, Scorpio, Pisces",
             21:"You are Aries, part of the Fire group, compatible with Aries, Leo, Sagittarius"},
          4:{19:"You are Aries, part of the Fire group, compatible with Aries, Leo, Sagittarius",
             20:"You are Taurus, part of the Earth group\ncompatible with Taurus, Virgo, Capricorn"},
          5:{20:"You are Taurus, part of the Earth group\ncompatible with Taurus, Virgo, Capricorn",
             21:"You are Gemini, part of the Air group\ncompatible with Gemini, Libra, Aquarius"},
          6:{21:"You are Gemini, part of the Air group\ncompatible with Gemini, Libra, Aquarius",
             22:"You are cancer, part of the Water group\ncompatible with Cancer, Scorpio, Pisces"},
          7:{22:"You are cancer, part of the Water group\ncompatible with Cancer, Scorpio, Pisces",
             23:"You are Leo, part of the Fire group, compatible with Aries, Leo, Sagittarius"},
          8:{22:"You are Leo, part of the Fire group, compatible with Aries, Leo, Sagittarius",
             23:"You are Virgo, part of the Earth group\ncompatible with Taurus, Virgo, Capricorn"},
          9:{22:"You are Virgo, part of the Earth group\ncompatible with Taurus, Virgo, Capricorn",
             23:"You are Libra, part of the Air group\ncompatible with Gemini, Libra, Aquarius"},
          10:{23:"You are Libra, part of the Air group\ncompatible with Gemini, Libra, Aquarius",
              24:"You are Scorpio, part of the Water group\ncompatible with Cancer, Scorpio, Pisces"},
          11:{21:"You are Scorpio, part of the Water group\ncompatible with Cancer, Scorpio, Pisces",
              22:"You are Sagittarius, part of the Fire group, compatible with Aries, Leo, Sagittarius"},
          12:{21:"You are Sagittarius, part of the Fire group, compatible with Aries, Leo, Sagittarius",
              22:"You are Capricorn, part of the Earth group\ncompatible with Taurus, Virgo, Capricorn"}}

def sign(x,y):
      z = list(x.keys())
      if y <= z[0]:
            print(x[z[0]])
      else:
            print(x[z[1]])
            
while True:
      print('please enter your birthday')
      month = int(input('month: '))
      day = int(input('day: '))
      if month in range(1,13):
            sign(zodiac[month], day)
      else:
            print('not a valid date')

'''
============== RESTART: C:\\Users\\aerin\\Documents\Python\\zodiac.py ==============
please enter your birthday
month: 5
day: 8
You are Taurus, part of the Earth group
compatible with Taurus, Virgo, Capricorn
please enter your birthday
month: -8
day: 3
not a valid date
please enter your birthday
month: 9
day: 19
You are Virgo, part of the Earth group
compatible with Taurus, Virgo, Capricorn
please enter your birthday
month: 
'''
