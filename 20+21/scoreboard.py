from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__(visible=False)
        self.color('white')
        self.teleport(0,350)
        self.write('Score: 0', font=('Arial', 16, 'normal'))
    def show_score(self, score):
        self.clear()
        self.write(f'Score: {score}', font=('Arial', 16, 'normal'))
