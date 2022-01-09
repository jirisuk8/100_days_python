import turtle
from turtle import Turtle, Screen
import random
turtle.colormode(255)
tim = Turtle()
# tim.shape("turtle")
# tim.color("red")

# for _ in range(30):
#     tim.color("red")
#     tim.forward(10)
#     tim.penup()
#     tim.forward(10)
#     tim.pendown()

# colors = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]

# def draw_shape(num_sides):
#     angle = 360/num_sides
#     for _ in range(num_sides):
#         tim.forward(100)
#         tim.right(angle)
#
#
# for num in range(2, 8):
#     tim.color(random.choice(colors))
#     draw_shape(num)


#### cesta
def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return r, g, b
#
# directions = [0, 90, 180, 270]
# tim.speed(0)
# tim.pensize(10)
#
# for _ in range(500):
#     tim.color(random_color())
#     tim.forward(30)
#     tim.setheading(random.choice(directions))


#### spirograph
tim.speed(0)
num_of_circles = 60
for _ in range(num_of_circles):
    tim.color(random_color())
    tim.circle(150)
    tim.left(360/num_of_circles)




screen = Screen()
screen.exitonclick()