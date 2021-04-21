# Program name: GUI.py
# Your Name: Aerin Schmall
# Python Version: 3.7.8
# Date Started - Date Finished: 11/11/2020 - 11/11/2020
# Description: GUI calculator
import tkinter as kinter

w = []
window = kinter.Tk()
window.title('CALCULATOR')
window.geometry('180x70')

e = kinter.Text(window, height=4, width=40)
e.grid(row=0, columnspan=4)
e.insert(kinter.END, '\n\n\n')

w.append(kinter.Button(window, text='0', width=23, height=5, command=lambda n=0: myFunction(0)))
w[0].grid(row=4, column=0, columnspan=2)

w.append(kinter.Button(window, text='=', width=11, height=11, command=lambda n=0: myFunction('=')))
w[1].grid(row=3, column=3, rowspan=2)

w.append(kinter.Button(window, text='1', width=11, height=5, command=lambda n=0: myFunction(1)))
w[2].grid(row=1, column=0)

w.append(kinter.Button(window, text='2', width=11, height=5, command=lambda n=0: myFunction(2)))
w[3].grid(row=1, column=1)

w.append(kinter.Button(window, text='3', width=11, height=5, command=lambda n=0: myFunction(3)))
w[4].grid(row=1, column=2)

w.append(kinter.Button(window, text='+', width=11, height=5, command=lambda n=0: myFunction('+')))
w[5].grid(row=1, column=3)

w.append(kinter.Button(window, text='4', width=11, height=5, command=lambda n=0: myFunction(4)))
w[6].grid(row=2, column=0)

w.append(kinter.Button(window, text='5', width=11, height=5, command=lambda n=0: myFunction(5)))
w[7].grid(row=2, column=1)

w.append(kinter.Button(window, text='6', width=11, height=5, command=lambda n=0: myFunction(6)))
w[8].grid(row=2, column=2)

w.append(kinter.Button(window, text='-', width=11, height=5, command=lambda n=0: myFunction('-')))
w[9].grid(row=2, column=3)

w.append(kinter.Button(window, text='7', width=11, height=5, command=lambda n=0: myFunction(7)))
w[10].grid(row=3, column=0)

w.append(kinter.Button(window, text='8', width=11, height=5, command=lambda n=0: myFunction(8)))
w[11].grid(row=3, column=1)

w.append(kinter.Button(window, text='9', width=11, height=5, command=lambda n=0: myFunction(9)))
w[12].grid(row=3, column=2)

w.append(kinter.Button(window, text='.', width=11, height=5, command=lambda n=0: myFunction('.')))
w[13].grid(row=4, column=2)

tt=0
def myFunction(button):
      global tt
      if tt == 1: 
            e.delete('1.0', '2.0')
            e.insert(kinter.END, '\n')# essentially a stack
            tt=0
      e.insert(kinter.END,button)

      eq = e.get('4.0', kinter.END)
      if button == '=':
            spliteq = eq.split('=')
            ans = eval(spliteq[0])
            e.insert(kinter.END,ans)
            tt = 1
            
'''
============= RESTART: C:\\Users\\aerin\\Documents\\Python\\GUI.py
'''
