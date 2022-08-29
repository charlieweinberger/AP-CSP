import random

class ninetyNine():

    def __init__(self, players):
        self.deck = 4 * ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']
        self.total = self.pick_random()
        self.players = players
        self.winner = None

    def pick_random(self):
        card = random(self.deck)
        self.deck.remove(card)
        return card

    def deal(self, n):
        for player in self.players:
            for i in range(n):
                player.hand.append(self.pick_random())

    def run():
        while self.winner == None:
            for player in self.players:
                self.total += player.turn()
                if self.total > 99:
                    self.winner = 3 - player.player_number

class nnPlayer():

    def __init__(self, player_number):
        self.hand = []
        self.player_number = player_number
    
    def turn(self):
        card = input(f"Your hand: {self.hand} \nWhat card do you want to play? ")
        if card not in self.hand: return
        if card == 'Ace': return int(input("Do you want your Ace to count as 1 or 11? "))
        if card in ['Jack', 'Queen', 'King']: return 10
        return int(card)

class nnComputerPlayer():
    
    def __init__(self, player_number):
        self.hand = []

    def turn(self):
        card = random.choice(self.hand)
        if card == 'Ace': return 1
        if card in ['Jack', 'Queen', 'King']: return 10
        return int(card)

players = [nnPlayer(1), nnComputerPlayer(2)]
nn = ninetyNine(players)
nn.deal(10)
nn.run()
print(nn.winner)