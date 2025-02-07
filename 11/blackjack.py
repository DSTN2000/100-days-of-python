from random import *

deck = sorted(([i for i in range(2,12)] + [10] * 3)*4)
#print(deck)

def hand_cards(object, ncards, deck=deck):
    '''Hands ncards to the object from the deck. Returns the updated object'''
    cards = []
    for _ in range(ncards):
        card = choice(deck)
        deck.remove(card)
        cards.append(card)
    object += cards
    return object

class Blackjack:
    '''The player's blackjack session'''
    def __init__(self, winner=None):
        self.start_game()
        self.reveal_cards()
        self.winner = winner
        match input('Type \'h\' to hit or \'s\' to stand: '):
            case 'h':
                self.hit()
            case 's':
                self.stand()
            case (_):
                exit()
    def start_game(self):
        hand_cards(player,2)
        hand_cards(dealer,2)
    def end_game(self):
        self.print_hands()
        self.set_winner()
    def reveal_cards(self):
        print(f'Your cards: {player}')
        print(f'The dealer\'s first card: {dealer[0]}')
    def hit(self):
        hand_cards(player,1)
        self.end_game()
    def stand(self):
        self.end_game()
    def set_winner(self):
        '''Find out who is closer to 21'''
        player_score = sum(player) if 11 not in player else sum(player)-10 if sum(player)>21 else sum(player)
        dealer_score = sum(dealer) if 11 not in dealer else sum(dealer)-10 if sum(dealer)>21 else sum(dealer)
        if player_score>dealer_score and player_score <= 21:
            self.winner = player
        elif player_score == dealer_score:
            pass
        else:
            self.winner = dealer
    def print_hands(self):
        print(f'Your final hand: {player}')
        print(f'The dealer\'s final hand: {dealer}')


player = []
dealer = []
blackjack = Blackjack()
match blackjack.winner:
    case winner if winner == player:
        print('You Won!')
    case winner if winner == dealer:
        print('The dealer Won!')
    case None:
        print('It is a tie!')
