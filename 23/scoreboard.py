from turtle import Turtle

FONT=('Arial', 25, 'normal')

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__(visible=False)
        self.highscore = 0
        with open('23/highscore.txt') as highscore:
            self.highscore = int(highscore.read())
        self.score = 0
        self.teleport(-80,350)
        self.color('black')
        self.game_over = False
        

    def show_score(self):
        if self.score > self.highscore:
            with open('23/highscore.txt', 'w') as highscore:
                highscore.write(str(self.score))
            self.highscore = self.score
        self.clear()
        self.write(f'Score: {self.score}', font=FONT)
        if self.game_over:
            self.teleport(-120,0)
            self.write(f'GAME OVER! Highscore: {self.highscore}', font=FONT)