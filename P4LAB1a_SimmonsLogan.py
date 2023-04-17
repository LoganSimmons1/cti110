# CTI-110
# P4LAB1a
# Logan Simmons
# 4/15/2023

# tess.forward(50)
# tess.left(120)
# tess.forward(50)
# tess.left(120)
# tess.forward(50)

# tess.left(30)
# tess.forward(50)          
# tess.left(90)      
# tess.forward(50)
# tess.left(90)
# tess.forward(50)
# tess.left(90)
# tess.forward(50)

import turtle
wn = turtle.Screen()
wn.bgcolor("lightblue")      
wn.title("P4LAB1a")      

tess = turtle.Turtle()
tess.color("blue")      
tess.pensize(3)

import turtle
turtle.showturtle()
for x in range(3):
    turtle.forward(50)
    turtle.left(120)

import turtle
turtle.showturtle()
for x in range(4):
    turtle.left(90)
    turtle.forward(50)
