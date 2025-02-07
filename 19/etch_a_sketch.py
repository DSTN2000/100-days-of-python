from turtle import *

class MyTurtle(Turtle):
    def __init__(self, *args, screen):
        super().__init__(*args)
        self.screen = screen
        self.control()

    def control(self):
        self.screen.onkey(key='w', fun=self.forward)
        self.screen.onkey(key='s', fun=self.backward)
        self.screen.onkey(key='d', fun=self.right)
        self.screen.onkey(key='a', fun=self.left)

        self.screen.onkey(key='c', fun=self.clear)

    def forward(self):
        super().forward(20)
    def backward(self):
        super().backward(20)
    def right(self):
        super().right(10)
    def left(self):
        super().left(10)
    def clear(self):
        super().clear()
        self.teleport(0,0)
        
screen = Screen()
turtle = MyTurtle('turtle', screen=screen)

turtle.speed(0)

screen.listen()

screen.exitonclick()