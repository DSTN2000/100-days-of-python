from turtle import *
from sep_line import SepLine
from scoreboard import Scoreboard
from ball import Ball
from paddle import Paddle
import time

SCREEN_WIDTH = 1920
SCREEN_HEIGHT = 1080
INITIAL_BALL_SPEED = 8
BALL_SPEED = INITIAL_BALL_SPEED
MAX_SPEED = 16
MAX_X = 740
MAX_Y = 400


screen = Screen()
screen.bgcolor('black')
screen.setup(SCREEN_WIDTH, SCREEN_HEIGHT, 0, 0)
screen.tracer(0)
screen.listen()

def control(p1_paddle,p2_paddle):
    screen.onkey(key='Up', fun=p2_paddle.up)
    screen.onkey(key='Down', fun=p2_paddle.down)
    screen.onkey(key='w', fun=p1_paddle.up)
    screen.onkey(key='s', fun=p1_paddle.down)


sep_line = SepLine(SCREEN_HEIGHT)
scoreboard = Scoreboard()
ball = Ball()
p1_paddle, p2_paddle = [Paddle() for _ in range(2)]
p1_paddle.teleport(-MAX_X,0)
p2_paddle.teleport(MAX_X,0)

def new_round():
    scoreboard.show_scores()
    p1_paddle.teleport(-MAX_X,0)
    p2_paddle.teleport(MAX_X,0)   
    ball.restart()
game_active = True
#initialize player controls
control(p1_paddle,p2_paddle)
while game_active:
    ball.forward(BALL_SPEED)
    if (ball.distance(p1_paddle) < 50 and ball.xcor() < -MAX_X+20) or (ball.distance(p2_paddle) < 50 and ball.xcor() > MAX_X-20):
        if BALL_SPEED < MAX_SPEED:
            BALL_SPEED *=1.05
        print(BALL_SPEED)
        ball.bounce_x()
    if ball.ycor() > MAX_Y or ball.ycor() < -MAX_Y:
        ball.bounce_y()
    if ball.xcor() > MAX_X:
        scoreboard.scores[0]+=1
        BALL_SPEED = INITIAL_BALL_SPEED 
        new_round()
    if ball.xcor() < -MAX_X:
        scoreboard.scores[1]+=1
        BALL_SPEED = INITIAL_BALL_SPEED 
        new_round()
    screen.update()
    time.sleep(1/64)

screen.exitonclick()