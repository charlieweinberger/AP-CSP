import random

class RandomPlayer():
    
    def __init__(self, player_number):
        self.hand = []
        self.player_number = player_number
        self.game = None

    def turn(self):
        
        card = random.choice(self.hand)
        self.hand.remove(card)
        
        print(f"\nYour opponent has played a {card}.")
        
        if card == 'Ace': return 1
        if card in ['Jack', 'Queen', 'King']: return 10
        return int(card)