from turtle import *
from random import *
import itertools
import time
from food import Food, MAX_X, MAX_Y 
from scoreboard import Scoreboard

MOVE_DISTANCE = 20

class SnakeBlock(Turtle):
    iter_id = itertools.count()
    def __init__(self, *args, screen):
        super().__init__(*args)
        self.shape('square')
        self.id = next(self.iter_id)
        self.color('white')
        self.penup()
        self.screen = screen

    def control(self):
        self.screen.onkey(key='Up', fun=self.up)
        self.screen.onkey(key='Down', fun=self.down)
        self.screen.onkey(key='Right', fun=self.right)
        self.screen.onkey(key='Left', fun=self.left)

    def up(self):
        new_heading = 90
        if abs(new_heading - self.heading()) != 180:
            super().setheading(new_heading)
    def down(self):
        new_heading = -90
        if abs(new_heading - self.heading()) != 180:
            super().setheading(new_heading)
    def right(self):
        new_heading = 0
        if abs(new_heading - self.heading()) != 180:
            super().setheading(new_heading)
    def left(self):
        new_heading = 180
        if abs(new_heading - self.heading()) != 180:
            super().setheading(new_heading)

class Snake(list):
    def __init__(self, screen):
        for _ in range(3):
            block = SnakeBlock(screen=screen)
            block.goto((-MOVE_DISTANCE)*block.id,0)
            self.append(block)
        self.scoreboard = Scoreboard()
        self.food = Food()
        self.head = self[0]
        self.screen = screen
        self.head.control()
        self.move_body()

    def move_body(self):
        '''Moves each subsequent block to the position of the next block and then moves the head in its direction.
        After that checks if food can be eaten'''
        game_over = False
        while True:
            for i in range(len(self)-1, 0, -1):
                self[i].goto(self[i-1].position())
            
            self.head.forward(MOVE_DISTANCE)
            if self.head.distance(self.food) < 1:
                    self.eat_food(self.food)
                    self.scoreboard.show_score(self.food.score)
                    continue
            time.sleep(1/18)
            self.screen.update()
            if self.head.xcor() > MAX_X or self.head.xcor() < -MAX_X \
            or self.head.ycor() > MAX_Y or self.head.ycor() < -MAX_Y:
                self.scoreboard.teleport(0,0)
                self.scoreboard.write('Game Over!', font=('Arial', 16, 'normal'))
                break
            for block in self[1::]:
                if block.distance(self.head) < 1:
                    self.scoreboard.teleport(0,0)
                    self.scoreboard.write('Game Over!', font=('Arial', 16, 'normal'))
                    game_over = True
                    break
            if game_over:
                break

    
    def eat_food(self, food):
        '''Teleports food and grows body by one block. Invoked from move_body'''
        food = self.food
        food.teleport()
        new_block = SnakeBlock(screen=self.screen)
        self.append(new_block)

                
