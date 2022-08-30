class MaxPlayer():
    
    def __init__(self, player_number):
        self.hand = []
        self.player_number = player_number
        self.game = None

    def turn(self):
        
        max_card = ''
        max_value = 0

        for card in self.hand:
            
            if card in ['Jack', 'Queen', 'King']:
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

        print(f"\nOpponent hand: {self.hand}\nYour opponent has played a {max_card}.")

        self.hand.remove(max_card)
        return max_value