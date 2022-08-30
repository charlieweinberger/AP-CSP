from nn import *
from input_player import *
from random_player import *
from max_player import *
from charlie_player import *

# a player can't play itself (aka random vs random doesn't work)

players_names = ['max', 'charlie'] # input, random, max, charlie

human_playing = 'input' in players_names
num_games = 1 if human_playing else 100000
winners = {player:0 for player in players_names}

for i in range(num_games):

    players = []

    for player in players_names:
        if player == 'input':   players.append(InputPlayer())
        if player == 'random':  players.append(RandomPlayer())
        if player == 'max':     players.append(MaxPlayer())
        if player == 'charlie': players.append(CharliePlayer())

    if i % 2 == 1:
        players = players[::-1]

    for j, player in enumerate(players):
        player.player_number = j + 1

    nn = ninetyNine(players, show=human_playing)
    nn.set_players()
    nn.deal(10)

    nn.run()

    for player in nn.players:
        if player.player_number == nn.winner:
            winners[player.name] += 1
            break

if not human_playing:
    print(f'Score after {num_games} games: {winners}')
    print(f'Win percent: {100 * max(winners.values()) / num_games}%')