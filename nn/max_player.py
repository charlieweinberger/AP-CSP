class MaxPlayer():
    
    def __init__(self):
        self.hand = []
        self.name = 'max'
        self.player_number = None
        self.game = None

    def turn(self):
        
        if len(self.hand) == 0:
            self.game.winner = 3 - self.player_number
            return

        max_card = ''
        max_value = 0

        for card in self.hand:
            
            if card in ['10', 'Jack', 'Queen', 'King']:
                max_card = card
                max_value = 10
                break
                
            if card in '23456789':
                if int(card) > max_value:
                    max_card = card
                    max_value = int(card)

            if card == 'Ace' and max_card == '':
                max_card = 'Ace'
                max_value = 1

        if self.game.show: print(f"\nOpponent hand: {self.hand}\nYour opponent has played a {max_card}.")

        self.hand.remove(max_card)
        return max_value