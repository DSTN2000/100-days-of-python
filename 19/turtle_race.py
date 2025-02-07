from turtle import *
from random import *
import itertools

screen = Screen()
screen.setup(1920, 1080, 0, 0)

class RaceTurtle(Turtle):
    iter_id = itertools.count()

    def __init__(self, *args, color):
        super().__init__(*args)
        self.color(color)
        self.id = next(self.iter_id)
        self.penup()
        self.goto(-screen.window_width()/2+100, -screen.window_height()/2+50+self.id*150)
        self.won_the_race = False
        

    def move(self):
        self.forward(randint(30,60))
        if self.xcor()>=screen.window_width()/2-100:
            self.won_the_race = True
        
class Race:
    def __init__(self, participants):
        self.status = 'active'
        self.winner = None
        self.participants = participants

    def race(self):
        while self.status == 'active':
            for participant in self.participants:
                participant.move()
                if participant.won_the_race:
                    race.status = 'finished'
                    race.winner = participant.id
                    break

class Bet(str):
    def __init__(self, *args):
        super().__init__()
        self.is_correct = None
        self.actual_winner = None

ROYGBP = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
race_turtles = {}
for color in ROYGBP:
    race_turtles[color] = RaceTurtle('turtle', color=color)
bet = Bet(screen.textinput(title='Make your bet',
                        prompt='Who will win the race?\nEnter a color'))

race = Race(race_turtles.values())
race.race()
print(f'The race winner is {ROYGBP[race.winner]}')
bet.actual_winner = ROYGBP[race.winner]
write(f'You made the {'winning' if bet==bet.actual_winner else 'wrong'} bet!\nThe actual winner is {ROYGBP[race.winner]}.')
screen.exitonclick()