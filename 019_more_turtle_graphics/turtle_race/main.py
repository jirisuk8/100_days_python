import turtle
from turtle import Turtle, Screen
import random


screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_positions = [-150, -90, -30, 30, 90, 150]
all_turtles = []
is_race_on = False

for turtle_index in range(len(colors)):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.speed(10)
    new_turtle.goto(x=-230, y=y_positions[turtle_index])
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() >= 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f'You won! Color {winning_color} was the fastest one.')
            else:
                print(f"You lost! Your color {user_bet} lost over winning {winning_color}")
            break

        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)







screen.exitonclick()