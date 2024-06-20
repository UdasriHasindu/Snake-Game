from turtle import Screen
from snake_blocks import Snake
from snake_classes import Food, ScoreBoard
import time

window = Screen()
window.setup(width=800, height=700)
window.bgcolor("#161616")
window.title("SNAKE GAME")
window.tracer(0)

snake = Snake()
ball = Food()
scores = ScoreBoard()


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

# detecting when snake eats food
    if snake.head.distance(ball) < 20:
        ball.refresh()
        scores.count_score()
        snake.expand()

    if snake.head.xcor() > 380 or snake.head.xcor() < -380 or snake.head.ycor() > 330 or snake.head.ycor() < -330:
        is_game_on = False
        scores.game_over()

    for block in snake.snake[1:]:
        if block.distance(snake.head) < 10:
            is_game_on = False
            scores.game_over()

window.exitonclick()
