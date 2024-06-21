from turtle import Turtle, Screen

def interpolate_color(start_color, end_color, factor):
    return (int(start_color[0] + (end_color[0] - start_color[0]) * factor),
            int(start_color[1] + (end_color[1] - start_color[1]) * factor),
            int(start_color[2] + (end_color[2] - start_color[2]) * factor))

def hex_color(rgb):
    return "#%02x%02x%02x" % rgb

# Set up the screen
window = Screen()
window.setup(width=900, height=800)
window.bgcolor("#161616")
window.title("SNAKE GAME")
window.tracer(0)

# Define boundaries
MAX_WIDTH_X = 400
MIN_WIDTH_X = -400
MAX_HEIGHT_Y = 350
MIN_HEIGHT_Y = -350

# Create a turtle object for the border
border = Turtle()
border.pensize(10)
border.penup()

# Define the gradient colors
start_color = (255, 0, 0)  # Red
end_color = (0, 0, 255)    # Blue

# Number of points for gradient effect
num_points = 100

# Function to draw a gradient line
def draw_gradient_line(turtle, start_pos, end_pos, start_color, end_color, num_points):
    start_x, start_y = start_pos
    end_x, end_y = end_pos
    delta_x = (end_x - start_x) / num_points
    delta_y = (end_y - start_y) / num_points

    for i in range(num_points + 1):
        factor = i / num_points
        color = hex_color(interpolate_color(start_color, end_color, factor))
        turtle.pencolor(color)
        x = start_x + i * delta_x
        y = start_y + i * delta_y
        turtle.goto(x, y)
        if i == 0:
            turtle.pendown()

# Draw the gradient border
border.goto(MIN_WIDTH_X, MAX_HEIGHT_Y)
draw_gradient_line(border, (MIN_WIDTH_X, MAX_HEIGHT_Y), (MAX_WIDTH_X, MAX_HEIGHT_Y), start_color, end_color, num_points)
draw_gradient_line(border, (MAX_WIDTH_X, MAX_HEIGHT_Y), (MAX_WIDTH_X, MIN_HEIGHT_Y), start_color, end_color, num_points)
draw_gradient_line(border, (MAX_WIDTH_X, MIN_HEIGHT_Y), (MIN_WIDTH_X, MIN_HEIGHT_Y), start_color, end_color, num_points)
draw_gradient_line(border, (MIN_WIDTH_X, MIN_HEIGHT_Y), (MIN_WIDTH_X, MAX_HEIGHT_Y), start_color, end_color, num_points)

# Update the screen to show the drawing
window.update()

# Keep the window open
window.mainloop()
