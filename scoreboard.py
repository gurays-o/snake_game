from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 16, "bold")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        with open("data.txt") as d:
            self.high_score = int(d.read())
        self.score_count = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 275)
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score_count} | Hi-Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def reset_game(self):
        if self.score_count > self.high_score:
            self.high_score = self.score_count
            with open("data.txt", mode="w") as f:
                f.write(str(self.high_score))

        self.score_count = 0
        self.update_score()

    def increase_score(self):
        self.score_count += 1
        self.update_score()
