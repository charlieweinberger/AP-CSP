points = {
    'Ronan': 0,
    'Cayden': 0,
    'William': 0,
    'Christine': 0
}

def add_points(player, number):
    points[player] += number

def show_points(player):
    print(points[player])

def cheater(player):
    points[player] = 0

def end_game():
    
    for player, num_points in points.items():
        print(f"{player} has {num_points} points.")
    
    # max(points, key=lambda key: points[key])

    print(f"{max(points, key=points.get)} has won!")

add_points('Ronan', 5)
show_points('Ronan')
add_points('William', 2)
cheater('William')
show_points('William')
end_game()