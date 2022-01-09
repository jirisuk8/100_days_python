from turtle import Turtle

UP = 90
DOWN = 270
MOVE_DISTANCE = 30


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.create_paddle(position)

    def create_paddle(self, position):
        self.shape("square")
        self.color("white")
        self.penup()
        self.turtlesize(stretch_wid=5, stretch_len=1)
        self.goto(position)

    def move_paddle_up(self):
        self.goto(self.xcor(), self.ycor()+MOVE_DISTANCE)

    def move_paddle_down(self):
        self.goto(self.xcor(), self.ycor()-MOVE_DISTANCE)

