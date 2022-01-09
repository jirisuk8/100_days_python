import colorgram
import turtle
from turtle import Turtle, Screen
import random

# cols = colorgram.extract('painting.jpg', 15)
# colors = []
#
# for c in cols:
#     rgb_representation = tuple(c.rgb)
#     colors.append(rgb_representation)
#
# colors = colors[7:]

colors = [(26, 108, 164), (193, 38, 81), (237, 161, 50), (234, 215, 86), (227, 237, 229), (223, 137, 176), (143, 108, 57), (103, 197, 219), (21, 57, 132), (205, 166, 30), (213, 74, 91), (238, 89, 49)]

turtle.colormode(255)
tim = Turtle()
tim.speed(0)
tim.penup()
# tim.penup()
# tim.setheading(225)
# tim.forward(200)
# tim.setheading(0)
# tim.pendown()


for i in range(10):
    for _ in range(10):
        tim.dot(20, random.choice(colors))
        tim.forward(30)
    tim.home()
    tim.left(90)
    tim.forward(30*(i+1))
    tim.right(90)




screen = Screen()
screen.exitonclick()