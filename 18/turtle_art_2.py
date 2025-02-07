import colorgram
from turtle import *
from random import *

turtle = Turtle('turtle')

def get_rgb_colors():
    colors = colorgram.extract('18/nature.jpg', 10)
    rgb_colors = []
    for color in colors:
        (r, g, b) = color.rgb
        rgb = (r,g,b)
        rgb_colors.append(rgb)
    return rgb_colors

rgb_colors = get_rgb_colors()

turtle.speed(0)
turtle.hideturtle()
colormode(255)
def draw(start_pos = (-350,-290),turtle=turtle):    
    turtle.teleport(*start_pos)
    for i in range(10):
        for j in range(10):   
            turtle.dot(20, choice(rgb_colors))
            turtle.teleport(turtle.xcor()+75, turtle.ycor())
        turtle.teleport(start_pos[0], turtle.ycor()+65)

draw()
screen = Screen()
screen.exitonclick()
