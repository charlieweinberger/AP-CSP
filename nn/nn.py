import random

class ninetyNine():

    def __init__(self, players, show = True):
        self.deck = 4 * ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']
        self.total = 0
        self.players = players
        self.show = show
        self.winner = None

    def set_players(self):
        for player in self.players:
            player.game = self

    def deal(self, n):
        for player in self.players:
            for _ in range(n):
                card = random.choice(self.deck)
                self.deck.remove(card)
                player.hand.append(card)

    def run(self):

        while self.winner == None:
            for player in self.players:
                
                turn = ''

                while type(turn) != int and self.winner == None:
                    turn = player.turn()

                if self.winner != None: break
                self.total += turn
                
                if self.show: print(f"Total: {self.total}")
                
                if self.total > 99:
                    self.winner = 3 - player.player_number
                    break
        
        if self.show:
            
            human_playing = False
            
            for player in self.players:
                if player.name == 'input':
                     print(f'\nYou {"win" if self.winner == player.player_number else "lose"}!')
                     human_playing = True
            
            if not human_playing:
                print(f'\nWinner: player {self.winner}!\n')