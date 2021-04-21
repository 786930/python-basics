# Program name: grocery.py
# Your Name: Aerin Schmall
# Python Version: 3.7.8
# Date Started - Date Finished: 11/11/2020 - 11/11/2020
# Description: creates class of items and calculates how many there are and total cost

class items:
      numberItems = 0

      def __init__ (self, name='apple', cost=2.49):
            self.itemName = name
            self.itemCost = cost

            items.numberItems += 1
      def show(self):
            print(self.itemName + ':', self.itemCost)
            
      def get(self):
            return self.itemName, self.itemCost
      
      def set(self):
            self.itemName = str(input('name of item: '))
            self.itemCost = float(input('cost: '))
            
eggs=items('eggs', 1.05)
milk=items('milk', 3.59)
carrots=items('carrots', 2.35)
bread=items('bread', 4)
apples=items()

groceryBag = [eggs, milk, carrots, bread, apples]

print(items.numberItems)

totalCost = 0
for i in groceryBag:
      a, b = i.get()
      totalCost += b
      
print(totalCost)
            
'''
============= RESTART: C:\\Users\\aerin\\Documents\\Python\\grocery.py =============
5
13.48
'''
