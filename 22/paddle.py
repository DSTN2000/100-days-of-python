from turtle import Turtle
from random import *

STEP_LENGTH = 50

class Paddle(Turtle):
    def __init__(self):
        super().__init__('square')
        self.speed(0)
        self.penup()
        self.setheading(90)
        self.shapesize(stretch_len=5, stretch_wid=0.5)
        self.color('white')
    
    def up(self):
        self.setheading(90)
        self.forward(STEP_LENGTH)
    def down(self):
        self.setheading(-90)
        self.forward(STEP_LENGTH)
        