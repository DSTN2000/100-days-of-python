from turtle import Turtle
import random

TILE_SIDE = 40
MAX_X = 740
ROYGBP = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']

class Car(Turtle):
    def __init__(self, spawn_position, direction, move_speed):
        super().__init__('square')
        self.y = spawn_position[1]
        self.move_speed = move_speed
        self.color(random.choice(ROYGBP))
        self.shapesize(1,random.randint(1,2))
        self.move_distance = TILE_SIDE
        self.setheading(direction)
        self.penup()
        self.teleport(*spawn_position)

    def move(self):
        self.forward(self.move_speed)
        if self.xcor() < -MAX_X-40:
            self.teleport(MAX_X+40,self.y)
        if self.xcor() > MAX_X+40:
            self.teleport(-MAX_X-40,self.y)