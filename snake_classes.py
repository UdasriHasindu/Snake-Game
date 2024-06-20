from turtle import Turtle
import random



# Creating foods in random places 
class Food(Turtle):

    def __init__(self):
        super().__init__()

        self.shape("circle")
        self.speed("fastest")
        self.color("red")
        self.penup()
        self.shapesize(.5, .5)
        self.refresh()

    def refresh(self):
        X_COORDINATES = random.randint(-380, 380)
        Y_COORDINATES = random.randint(-330, 330)
        self.setpos(X_COORDINATES, Y_COORDINATES)


#creating Score bord

FONT = ('Courier', 18, 'normal')
TEXT_ALIGN = 'center'


class ScoreBoard(Turtle):

    def __init__(self):

        super().__init__()

        self.score = 0
        self.hideturtle()
        self.penup()
        self.setpos(x=0, y=310)
        self.color("white")
        self.count_score()

    def count_score(self):
        self.clear()
        self.write(f"Score = {self.score} ", align=TEXT_ALIGN, font=FONT)
        self.score += 1

    def game_over(self):
        self.setpos(0, 0)
        self.write(f"Game Over", align=TEXT_ALIGN, font=FONT)


