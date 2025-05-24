from turtle import Turtle

FONT = ("Arial", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.level = 1
        self.penup()
        self.hideturtle()
        self.color("white")
        self.goto(-240, 260)
        self.display_level()

    def display_level(self):
        self.write(f"Level: {self.level}", align="center", font=FONT)

    def update_level(self):
        self.clear()
        self.level += 1
        self.write(f"Level: {self.level}", align="center", font=FONT)


    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over!", align="center", font=FONT)
