from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 20, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = self.load_high_score()
        self.color("white")
        self.penup()
        self.goto(0, 265)
        self.hideturtle()
        self.update_scoreboard()

    @staticmethod
    def load_high_score():
        with open('data.txt', "r") as f:
            return int(f.read())

    @staticmethod
    def write_high_score(score):
        with open('data.txt', "w") as f:
            f.write(score)

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} /// High score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def reset_scoreboard(self):
        if self.score > self.high_score:
            self.high_score = self.score
            self.write_high_score(f'{self.score}')
        self.score = 0
        self.update_scoreboard()

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()
