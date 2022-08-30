import random

class RandomPlayer():
    
    def __init__(self, player_number):
        self.hand = []
        self.player_number = player_number
        self.game = None

    def turn(self):
        
        if len(self.hand) == 0:
            self.game.winner = 3 - self.player_number
            return

        card = random.choice(self.hand)
        if self.game.show: print(f"\nOpponent hand: {self.hand}\nYour opponent has played a {card}.")
        self.hand.remove(card)
                
        if card == 'Ace': return 1
        if card in ['Jack', 'Queen', 'King']: return 10
        return int(card)