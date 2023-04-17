# CTI-110
# P4LAB1b
# Logan Simmons
# 4/16/2023

# import turtle
# do colors/pen settings
# draw an L
# use penup to move inline with L
# draw an S

import turtle
wn = turtle.Screen()
wn.bgcolor("lightblue")      
wn.title("P4LAB1b")      

turtle = turtle.Turtle()
turtle.color("blue")      
turtle.pensize(3)

turtle.right(90)
turtle.forward(60)
turtle.left(90)
turtle.forward(40)

turtle.penup()
turtle.forward(20)
turtle.left(90)
turtle.forward(60)
turtle.right(90)
turtle.forward(40)
turtle.pendown()

turtle.left(180)
turtle.forward(40)
turtle.left(90)
turtle.forward(30)
turtle.left(90)
turtle.forward(40)
turtle.right(90)
turtle.forward(30)
turtle.right(90)
turtle.forward(40)
