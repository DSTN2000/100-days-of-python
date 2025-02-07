from turtle import *
from player import Player
from row_spawner import *
from scoreboard import Scoreboard
import time

SCREEN_WIDTH = 1920
SCREEN_HEIGHT = 1080



screen = Screen()
screen.bgcolor('white')
screen.title('Turtle crossing')
screen.setup(SCREEN_WIDTH, SCREEN_HEIGHT, 0, 0)


def control(player):
    screen.onkey(key='Up', fun=player.up)
    screen.onkey(key='Down', fun=player.down)
    screen.onkey(key='Right', fun=player.right)
    screen.onkey(key='Left', fun=player.left)


def new_round(score_copy):
    screen.tracer(0)
    screen.listen()
    game_active = True
    player = Player()
    scoreboard = Scoreboard()
    scoreboard.score = score_copy
    scoreboard.show_score()

    row_spawners = []
    cars = []
    for y in range(len(ROWS_Y_COORDINATES)):
        row_spawner = RowSpawner()
        cars+=row_spawner.fill_row()
        row_spawners.append(row_spawner)


    #initialize player controls
    control(player)
    while game_active:
        for car in cars:
            if car.ycor() == round(player.ycor()):
                if car.distance(player) < 20:
                    game_active = False
                    scoreboard.game_over = True
                    scoreboard.show_score()
                    screen.update()
                    return

            car.move()
        for row_spawner in row_spawners:
            if row_spawner.y_coordinate == round(player.ycor()):
                if scoreboard.score < row_spawner.id+1:
                    scoreboard.score = row_spawner.id+1
                    scoreboard.show_score()
                else:
                    break
        if player.ycor() > MAX_Y:
            print('test', player.ycor())
            score_copy = scoreboard.score
            screen.clearscreen()
            new_round(score_copy)
            return
        screen.update()


    #time.sleep(1/1000)
new_round(0)
screen.exitonclick()