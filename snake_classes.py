from turtle import Turtle
import random



# Creating the wall around the window 
MAX_WIDTH_X = 410
MIN_WIDTH_X = -410
MAX_HEIGHT_Y = 350
MIN_HEIGHT_Y = -350

class Wall(Turtle):

    def __init__(self) :

        super().__init__()

        self.pencolor("white")
        self.hideturtle()
        self.pensize(10)
        self.penup()
        self.setpos(MIN_WIDTH_X, MAX_HEIGHT_Y)
        self.create_wall()

    def create_wall(self):

        self.pendown()
        self.goto(MAX_WIDTH_X, MAX_HEIGHT_Y)
        self.goto(MAX_WIDTH_X, MIN_HEIGHT_Y)
        self.goto(MIN_WIDTH_X, MIN_HEIGHT_Y)
        self.goto(MIN_WIDTH_X, MAX_HEIGHT_Y)


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
        self.setpos(x=0, y=360)
        self.color("white")
        self.count_score()

    def count_score(self):
        self.clear()
        self.write(f"Score = {self.score} ", align=TEXT_ALIGN, font=FONT)
        self.score += 1

    def game_over(self):
        self.setpos(0, 0)
        self.write(f"Game Over", align=TEXT_ALIGN, font=FONT)


