from turtle import *
from random import *

turtle = Turtle('turtle')
turtle.color('green')

def square(turtle):
    for _ in range(4):
        turtle.forward(100)
        turtle.left(90)

def dashed_line(turtle, distance, step=10):
    for _ in range(int(distance/step)):
        turtle.forward(step)
        [turtle.penup, turtle.pendown][_%2]()

hex = '01234567890ABCDEF'
def random_color():
    return f'#{''.join([choice(hex) for _ in range(6)])}'

def n_gon(n, color, turtle=turtle, side=100):
    turtle.color(color)
    for _ in range(n):
        turtle.forward(side)
        turtle.right(360/n)

turtle.speed(0)

# for _ in range(1000):
#     turtle.width(choice(range(10,21)))
#     turtle.color(random_color())
#     turtle.setheading(0.0001*choice(range(3600001)))
#     turtle.forward(30)

for i in range(360):
    turtle.color(random_color())
    turtle.circle(100)
    turtle.right(1)


screen = Screen()
screen.exitonclick()