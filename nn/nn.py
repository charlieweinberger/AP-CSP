import random

class ninetyNine():

    def __init__(self, players):
        self.deck = 4 * ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']
        self.total = 0
        self.players = players
        self.winner = None

    def set_players(self):
        for player in self.players:
            player.game = self

    def deal(self, n):
        for player in self.players:
            for i in range(n):
                card = random.choice(self.deck)
                self.deck.remove(card)
                player.hand.append(card)

    def run(self):
        while self.winner == None:
            for player in self.players:
                self.total += player.turn()
                print(f"Total: {self.total}")
                if self.total > 99:
                    self.winner = 3 - player.player_number
                    break