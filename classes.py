# Program name: classes.py
# Your Name: Aerin Schmall
# Python Version: 3.7.8
# Date Started - Date Finished: 11/11/2020 - 11/11/2020
# Description: records date and shows date

class date:
      def setDate(self):
            self.date = str(input('pleasee enter a date in MM/DD/YY format: '))
            self.month = self.date[:2]
            self.day = self.date[3:5]
            self.year = self.date[6:]
      def showDate(self):
            print(f'the date is {self.month}/{self.day}/{self.year}')
Date = date()

Date.setDate()
Date.showDate()
'''
============= RESTART: C:\\Users\\aerin\\Documents\\Python\\classes.py =============
pleasee enter a date in MM/DD/YY format: 01/10/06
the date is 01/10/06
'''
