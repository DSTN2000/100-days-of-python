from turtle import *
from random import *
from snake import Snake

screen = Screen()
screen.setup(1920, 1080, 0, 0)
screen.bgcolor('black')
screen.title('Snake')
screen.listen()
screen.tracer(0)

# food = Food()
snake = Snake(screen)


screen.exitonclick()