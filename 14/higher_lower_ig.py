from random import *

def fetch_data():
    '''Returns the data about the top 50 most followed IG accounts from Wikipedia'''

    res = []

    import requests
    from bs4 import BeautifulSoup as bs

    url = 'https://en.wikipedia.org/wiki/List_of_most-followed_Instagram_accounts'

    responce = requests.get(url)
    soup = bs(responce.text, 'html.parser')
    table = soup.find_all('table')[0]

    rows = table.find_all('tr')

    for row in rows[1:-2]:
        cells = row.find_all('td')
        data = [cell.text.strip().replace('\xa0', ', ') for cell in cells]
        data = {'name': data[1], 'followers': float(data[3]), 'profession': data[4], 'country': data[-1]}
        res.append(data)

    return res

def pick_random(list_):
    '''Returns and deletes a random item from a list'''
    res = choice(list_)
    list_.remove(res)
    return res

class HigherLower:
    '''A higher-lower game session'''
    def __init__(self, data, score=0, active=True):
        self.data = data
        self.score = score
        self.active = active
        self.options = [pick_random(data) for _ in range(2)]

    def choose(self):
        '''Pick one of the options and see if you were right. If your guess is correct, a new option will be picked'''
        selected_option = input('Who has more followers? Type 1 or 2: ')
        try:
            match selected_option:
                case '1':
                    if self.options[0]['followers'] >= self.options[1]['followers']:
                        print('You are right!')
                        self.display_answers()
                        self.options[1] = pick_random(data)
                        self.score += 1
                    else:
                        self.display_answers()
                        print('Game over!', f'Total score: {self.score}', sep='\n')
                        self.active = False
                case '2':
                    if self.options[1]['followers'] >= self.options[0]['followers']:
                        print('You are right!')
                        self.display_answers()
                        self.options[0] = self.options[1]
                        self.options[1] = pick_random(data)
                        self.score += 1
                    else:
                        print('Game over!', f'Total score: {self.score}', sep='\n')
                        self.display_answers()
                        self.active = False
                case (_):
                    self.display_answers()
                    self.active = False
        except IndexError:
            print('You won!')
            self.active = False

    def display_options(self):
        '''Shows the two available options to pick from and the current score'''
        print(f'Current score: {self.score}')
        res = []
        for option in self.options:
            res.append(f'{option['name']}, {option['profession']} from {option['country']}')
        print('\nVS\n'.join(res))

    def display_answers(self):
        '''Shows who has more followers'''
        for option in self.options:
            print(f'{option['name']} has {option['followers']} Million followers')
        

data = fetch_data()
game = HigherLower(data)
while game.active:
    game.display_options()
    print()
    game.choose()
    print('\n'*2)
    