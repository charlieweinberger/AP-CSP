from nn import *
from input_player import *
from random_player import *
from max_player import *
from charlie_player import *

winners = {1: 0, 2: 0}

for _ in range(100000):

    players = [MaxPlayer(1), CharliePlayer(2)]
    nn = ninetyNine(players, show=False)
    nn.set_players()
    nn.deal(10)

    nn.run()

    winners[nn.winner] += 1

print(winners)
print(f'Win percent: {100 * winners[2] / (winners[1] + winners[2])}%')

# wins ~85% percent of time against random and max player