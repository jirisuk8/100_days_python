from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 45, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score_1 = 0
        self.score_2 = 0
        self.hideturtle()
        self.penup()
        self.goto(0, 240)
        self.color("white")
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"{self.score_1}     {self.score_2}", move=False, align=ALIGNMENT, font=FONT)