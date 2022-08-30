from nn import *
from input_player import *
from random_player import *
from max_player import *
from charlie_player import *

players = [InputPlayer(1), CharliePlayer(2)]
nn = ninetyNine(players)
nn.set_players()
nn.deal(10)

nn.run()

print(f"\nWinner: Player {nn.winner}!")