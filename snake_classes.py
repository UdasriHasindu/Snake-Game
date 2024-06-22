from turtle import Turtle
import random

# Creating the wall around the window 
MAX_WIDTH_X = 420
MIN_WIDTH_X = -420
MAX_HEIGHT_Y = 355
MIN_HEIGHT_Y = -355

class Wall(Turtle):

    def __init__(self):
        super().__init__()
        self.pencolor("#973131")
        self.hideturtle()
        self.pensize(15)
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
        self.color("#A7E6FF")
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
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"Score = {self.score} ", align=TEXT_ALIGN, font=FONT)

    def count_score(self, game_mode):
        if game_mode == 'e' or game_mode == 'easy':
            self.score += 1
        elif game_mode == 'm' or game_mode == 'medium':
            self.score += 2
        elif game_mode == 'h' or game_mode == 'hard':
            self.score += 3
        self.update_score()

    def game_over(self):
        self.setpos(0, 300)
        self.write(f"Oopss..Game Over", align=TEXT_ALIGN, font=FONT)
