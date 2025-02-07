from turtle import Turtle
from car import TILE_SIDE, Car
import itertools
import random

MAX_X = 740
MAX_Y = 400
OBSTACLE_OFFSET = 120
OBSTACLE_MIN_Y = -MAX_Y + OBSTACLE_OFFSET
ROWS_Y_COORDINATES = [y for y in range(OBSTACLE_MIN_Y, MAX_Y+1, TILE_SIDE)]

class RowSpawner:

    iter_id = itertools.count()

    def __init__(self):
        self.id = next(self.iter_id)
        self.y_coordinate = ROWS_Y_COORDINATES[self.id%len(ROWS_Y_COORDINATES)]

    def fill_row(self):
        cars = []
        tiles_x_coordinates = [x for x in range(-MAX_X, MAX_X+1, TILE_SIDE)]
        row_direction = random.choice([0,180])
        row_speed = random.choice([1,2])
        cars_spawn_positions = [(tiles_x_coordinates[i+random.randint(1,4)],self.y_coordinate) for i in range(0,len(tiles_x_coordinates)-4,5)]
        for spawn_position in cars_spawn_positions:
            new_car = Car(spawn_position,row_direction, row_speed)
            cars.append(new_car)
        return cars