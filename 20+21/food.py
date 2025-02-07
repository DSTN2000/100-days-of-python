from turtle import Turtle
from random import choice

MAX_X = int(1920/2-220)
MAX_Y = int(1080/2-140)
X_VARS = [i for i in range(0,MAX_X,20)]
Y_VARS = [i for i in range(0,MAX_Y,20)]
SIGN = [-1,1]

class Food(Turtle):
    def __init__(self):
        super().__init__('circle')
        self.color('blue')
        self.score = -1
        self.teleport()

    def teleport(self):
        self.coordinates = (choice(SIGN) * choice(X_VARS), choice(SIGN) * choice(Y_VARS))
        #print(self.coordinates)
        super().teleport(*self.coordinates)
        self.score += 1
        
