from turtle import Screen
from snake_classes import Snake, Wall, Food, ScoreBoard
import time

# Defining the game mode
EASY = 0.5
MEDIUM = 0.1
HARD = 0.05

window = Screen()
window.setup(width=900, height=800)
window.bgcolor("#161616")
window.title("SNAKE GAME")
window.tracer(0)
game_mode = (window.textinput("Mode", "Easy , Medium or Hard [E / M / H]")).lower()
print(game_mode)

snake = Snake()
wall = Wall()
ball = Food()
scores = ScoreBoard()


window.listen()
window.onkey(snake.up, "Up")
window.onkey(snake.down, "Down")
window.onkey(snake.left, "Left")
window.onkey(snake.right, "Right")



is_game_on = True
while is_game_on:

    if (game_mode ==  'e') or (game_mode == 'easy'):
        speed = EASY
    elif (game_mode == 'm') or (game_mode == 'medium'):
        speed = MEDIUM
    elif( game_mode == 'h') or (game_mode == 'hard'):
        speed = HARD

    snake.move()
    window.update()
    time.sleep(speed)

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
