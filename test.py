from turtle import Turtle, Screen

window = Screen()
window.setup(width=800, height=700)
window.bgcolor("#161616")
window.title("SNAKE GAME")


MAX_WIDTH_X = 400
MIN_WIDTH_X = -400
MAX_HEIGHT_Y = 350
MIN_HEIGHT_Y = -350


line = Turtle()
line.pencolor("white")
line.pensize(10)
line.penup()

line.setpos(MIN_WIDTH_X, MAX_HEIGHT_Y)
line.pendown()
line.goto(MAX_WIDTH_X, MAX_HEIGHT_Y)
line.goto(MAX_WIDTH_X, MIN_HEIGHT_Y)
line.goto(MIN_WIDTH_X, MIN_HEIGHT_Y)
line.goto(MIN_WIDTH_X, MAX_HEIGHT_Y)












window.exitonclick()