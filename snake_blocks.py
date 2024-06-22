from turtle import Turtle

FORWARD_MOVES = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

# Colors for snake decoration
SNAKE_COLORS = ["#76B041", "#77D353", "#98FB98"]  # Example gradient colors

# Creating Snake blocks 
class Snake:

    def __init__(self):
        self.snake = []
        self.create_snake()
        self.head = self.snake[0]
        self.left_eye = self.create_eye((-5, 5))
        self.right_eye = self.create_eye((5, 5))

    def create_snake(self):
        for i in range(3):
            blocks = Turtle()
            blocks.penup()
            blocks.shape("square")
            blocks.color(SNAKE_COLORS[i % len(SNAKE_COLORS)])
            blocks.setpos(x=-(i * 20), y=0)
            self.snake.append(blocks)

    def create_eye(self, position):
        eye = Turtle()
        eye.penup()
        eye.shape("circle")
        eye.color("white")
        eye.shapesize(0.2, 0.2)  # Adjust the size as needed
        eye.setpos(self.head.xcor() + position[0], self.head.ycor() + position[1])
        return eye

    def update_eyes_position(self):
        self.left_eye.setpos(self.head.xcor() - 5, self.head.ycor() + 5)
        self.right_eye.setpos(self.head.xcor() + 5, self.head.ycor() + 5)

    def expand(self):
        blocks = Turtle()
        blocks.penup()
        blocks.shape("square")
        blocks.color(SNAKE_COLORS[len(self.snake) % len(SNAKE_COLORS)])
        blocks.setpos(self.snake[-1].position())
        self.snake.append(blocks)

    def move(self):
        # catch the tail of snake
        for block in range(len(self.snake) - 1, 0, -1):
            new_x = self.snake[block - 1].xcor()
            new_y = self.snake[block - 1].ycor()
            self.snake[block].setpos(x=new_x, y=new_y)

        self.head.forward(FORWARD_MOVES)
        self.update_eyes_position()

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
