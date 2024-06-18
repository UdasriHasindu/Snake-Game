from turtle import Turtle, Screen
from snake_classes import Snake, Food
import time

window = Screen()
window.setup(width=800, height=700)
window.bgcolor("#161616")
window.title("SNAKE GAME")
window.tracer(0)

snake = Snake()
ball = Food()


window.listen()
window.onkey(snake.up, "Up")
window.onkey(snake.down, "Down")
window.onkey(snake.left, "Left")
window.onkey(snake.right, "Right")


is_game_on = True
while is_game_on:

    snake.move()
    window.update()
    time.sleep(.08)
window.exitonclick()

