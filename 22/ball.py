from turtle import Turtle
from random import *

class Ball(Turtle):
    def __init__(self):
        super().__init__('circle')
        self.speed(0)
        self.color('white')
        self.penup()
        self.restart()
    
    def restart(self):
        self.teleport(0,0)
        self.setheading(randint(-28, 28)+choice([0,180]))

        
    def bounce_x(self):
        #TODO
        self.setheading(180-self.heading())
    def bounce_y(self):
        #TODO
        self.setheading(-self.heading())