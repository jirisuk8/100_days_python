from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()


screen.update()

screen.listen()
screen.onkeypress(r_paddle.move_paddle_up, "Up")
screen.onkeypress(r_paddle.move_paddle_down, "Down")

screen.onkeypress(l_paddle.move_paddle_up, "w")
screen.onkeypress(l_paddle.move_paddle_down, "s")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(ball.moving_speed)
    ball.move()

    # Detect collision with up and down wall
    if ball.ycor() >= 290 or ball.ycor() < -290:
        # need to bounce
        ball.wall_bounce()

    # Detect collision with paddle
    if (ball.distance(r_paddle) < 50 and ball.xcor() > 320) or (ball.distance(l_paddle) < 50 and ball.xcor() < -320):
        ball.paddle_bounce()

    # Detect ball passing by the right paddle
    if ball.xcor() > 400:
        ball.ball_reset()
        scoreboard.score_1 += 1
        scoreboard.update_scoreboard()

    # Detect ball passing by the left paddle
    if ball.xcor() < -400:
        ball.ball_reset()
        scoreboard.score_2 += 1
        scoreboard.update_scoreboard()


screen.exitonclick()
