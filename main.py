from turtle import Screen
from snake_blocks import Snake
from snake_classes import Wall, Food, ScoreBoard
import time

# Defining the game mode
EASY = 0.3
MEDIUM = 0.1
HARD = 0.05


# main function 
def start_game():

    # player screen
    window = Screen()
    window.setup(width=900, height=800)
    window.bgcolor("#1A1A1D")
    window.title("SNAKE GAME")
    window.tracer(0)

    snake = Snake()
    wall = Wall()
    ball = Food()
    scores = ScoreBoard()

    game_mode = (window.textinput("Mode", "Easy , Medium or Hard [E / M / H]")).lower()

    # make the snake head to listen the key commands 
    window.listen()
    window.onkey(snake.up, "Up")
    window.onkey(snake.down, "Down")
    window.onkey(snake.left, "Left")
    window.onkey(snake.right, "Right")

    is_game_on = True
    global speed
    while is_game_on:
        if game_mode == 'e' or game_mode == 'easy':
            speed = EASY
        elif game_mode == 'm' or game_mode == 'medium':
            speed = MEDIUM
        elif game_mode == 'h' or game_mode == 'hard':
            speed = HARD

        wall.create_wall()
        snake.move()
        window.update()
        time.sleep(speed)

        # detecting when snake eats food
        if snake.head.distance(ball) < 20:
            ball.refresh()
            scores.count_score(game_mode)
            snake.expand()

        # detecting collision with wall
        if snake.head.xcor() > 380 or snake.head.xcor() < -380 or snake.head.ycor() > 320 or snake.head.ycor() < -320:
            is_game_on = False
            scores.game_over()

        # detecting collision with itself
        for block in snake.snake[1:]:
            if block.distance(snake.head) < 10:
                is_game_on = False
                scores.game_over()

    # option to play again 
    def want_to_continue():
        play_again = (window.textinput("Play Again", "Want to continue [Y/N]")).lower()
        return play_again == 'y'

    if want_to_continue():
        window.clear()
        start_game()
    # else:
    #     window.exitonclick()


start_game()
