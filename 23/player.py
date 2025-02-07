from turtle import Turtle

TILE_SIDE = 40

class Player(Turtle):
    def __init__(self):
        super().__init__('turtle')
        self.color('green')
        self.shapesize(2,2)
        self.move_distance = TILE_SIDE
        self.setheading(90)
        self.penup()
        self.teleport(0,-360)

    def up(self):
        self.setheading(90)
        self.forward(self.move_distance)
    
    def down(self):
        self.setheading(-90)
        self.forward(self.move_distance)
        
    def right(self):
        self.setheading(0)
        self.forward(self.move_distance)
    
    def left(self):
        self.setheading(180)
        self.forward(self.move_distance)