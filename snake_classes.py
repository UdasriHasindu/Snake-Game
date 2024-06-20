from turtle import Turtle
import random

FORWARD_MOVES = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

# Creating Snake blocks 
class Snake:

    def __init__(self):
        self.snake = []
        self.create_snake()
        self.head = self.snake[0]

    def create_snake(self):
        for i in range(3):
            blocks = Turtle()
            blocks.penup()
            blocks.shape("square")
            blocks.color("white")
            blocks.setpos(x=-(i * 20), y=0)
            self.snake.append(blocks)

    def expand(self):
        blocks = Turtle()
        blocks.penup()
        blocks.shape("square")
        blocks.color("white")
        blocks.setpos(self.snake[-1].position())
        self.snake.append(blocks)

    def move(self):
        # catch the tail of snake
        for block in range(len(self.snake) - 1, 0, -1):
            new_x = self.snake[block - 1].xcor()
            new_y = self.snake[block - 1].ycor()
            self.snake[block].setpos(x=new_x, y=new_y)

        self.head.forward(FORWARD_MOVES)


    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)


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


