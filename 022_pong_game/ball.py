from turtle import Turtle

SPEED = 0.06

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.moving_speed = SPEED

    def move(self):
        self.goto(self.xcor()+self.x_move, self.ycor()+self.y_move)

    def wall_bounce(self):
        self.y_move *= -1

    def paddle_bounce(self):
        self.x_move *= -1
        self.moving_speed *= 0.9

    def ball_reset(self):
        self.goto(0, 0)
        self.moving_speed = SPEED
        self.x_move *= -1
