import random

class CharliePlayerV2():
    
    def __init__(self):
        self.hand = []
        self.name = 'charlie v2'
        self.player_number = None
        self.game = None

    def turn(self):
        
        if len(self.hand) == 0:
            self.game.winner = 3 - self.player_number
            return

        if 'Ace' in self.hand and (self.game.total == 88 or self.game.total == 98):
            return self.end_turn('Ace', 99 - self.game.total)

        return self.get_max()

    def get_max(self):

        max_card = ''
        max_value = 0

        for card in self.hand:
            
            if card in ['10', 'Jack', 'Queen', 'King'] and self.game.total < 90:
                max_card = card
                max_value = 10
                break
                
            if card in '23456789' and self.game.total < 100 - int(card):
                if int(card) > max_value:
                    max_card = card
                    max_value = int(card)

            if card == 'Ace' and max_card == '':
                max_card = 'Ace'
                max_value = 1

        if max_card == '': 
            max_card = random.choice(self.hand)
            if max_card == 'Ace': max_value = 1
            elif max_card in ['Jack', 'Queen', 'King']: max_value = 10
            else: max_value = int(max_card)
        
        return self.end_turn(max_card, max_value)
    
    def end_turn(self, card, value):
        if self.game.show: print(f"\nOpponent hand: {self.hand}\nYour opponent has played a {card}.")
        self.hand.remove(card)
        return value