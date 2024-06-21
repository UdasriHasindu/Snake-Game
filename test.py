from turtle import Turtle, Screen

window = Screen()
window.setup(width=900, height=800)
window.bgcolor("#161616")
window.title("SNAKE GAME")
window.tracer(0)


MAX_WIDTH_X = 400
MIN_WIDTH_X = -400
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

        

wall = Wall()
wall.create_wall()
window.update()



window.mainloop()