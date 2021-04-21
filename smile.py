# Program name: smile.py
# Your Name: Aerin Schmall
# Python Version: 3.7.8
# Date Started - Date Finished: 11/12/2020 - 11/12/2020
# Description: draws a smile
import turtle

draw = turtle.Turtle()


draw.pencolor("black")
draw.pendown()
draw.circle(100)

draw.penup()
draw.goto(-40, 110)
draw.pencolor("blue")
draw.pendown()
draw.circle(10)

 
draw.penup()
draw.goto(40, 110)
draw.pencolor("green")
draw.pendown()
draw.circle(10)
 

draw.penup()
draw.goto(0, 50)
draw.pencolor("red")
draw.pendown()
draw.circle(50, -50)
draw.circle(50, 100)

draw.penup()
draw.goto(0, 110)
draw.pencolor("brown")
draw.pendown()
draw.setheading(-90)
draw.forward(30)
'''
============= RESTART: C:\\Users\\aerin\\Documents\\Python\\smile.py
'''
