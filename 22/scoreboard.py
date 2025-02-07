from turtle import Turtle

FONT=('Arial', 25, 'normal')

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__(visible=False)
        self.scores = [0,0]
        self.teleport(-80,350)
        self.color('white')
        self.write('0\t0', font=FONT)
    def show_scores(self):
        self.clear()
        self.write(f'{self.scores[0]}\t{self.scores[1]}', font=FONT)