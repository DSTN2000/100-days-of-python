from turtle import Turtle

class SepLine(Turtle):
    def __init__(self, distance, step=10):
        super().__init__(visible=True)
        self.speed(0)
        self.teleport(0,-500)
        self.setheading(90)
        self.color('white')
        for _ in range(int(distance/step)):
            self.forward(step)
            [self.penup, self.pendown][_%2]()