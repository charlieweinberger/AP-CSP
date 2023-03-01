import random

# initialize variables

doors = [0, 0, 0]  # 0 = goat, 1 = car

# randomly assign the car behind one of the doors

car_index = random.randint(0, 2)
doors[car_index] = 1

# the player selects a door

print("Welcome to the Monty Hall Problem! In front of you, you will find three doors!")
print("[DOOR 1] [DOOR 2] [DOOR 3]")
print("Behind one of these doors is a brand! new! car!!!! Behind the other two...a mean, annoying GOAT!")

selected_door_index = int(input("CHOOSE WISELY! CHOOSE NOW! (1, 2, or 3): ")) - 1

def select_reveal_door():

    # FINISH THIS CODE TO CHOOSE A DOOR TO REVEAL
    # THE DOOR SHOULD HAVE A GOAT BEHIND IT BUT SHOULD NOT BE THE DOOR THE PLAYER HAS CHOSEN

    goat_door_indices = [i for i in range(len(doors)) if doors[i] == selected_door_index]
    return random.choice(goat_door_indices) + 1

revealed_door = select_reveal_door()

print(f"YOU HAVE CHOSEN DOOR {selected_door_index + 1}")
print(f"I CAN REVERAL TO YOU THAT {revealed_door} IS NOT HIDING A CAR!")

switch_response = input("Would you like to switch? Y or N? ").upper()

def end_game():

    print(selected_door_index)

    # BASED ON THE PLAYERS SWITCH CHOICE, DECIDE IF THE PLAYER HAS WON
    # RETURN THE WIN SCENARIO (TRUE/FALSE/ETC)

    if switch_response == 'Y':
        for i in range(len(doors)):
            if i != selected_door_index and i != revealed_door:
                selected_door_index = i
                break

    if doors[selected_door_index] == 1:
        return "YOU WIN!"
    else:
        return "YOU LOSE!"

print(selected_door_index)

# PRINT THE WIN/LOSS SCENARIO
print(end_game())

## MONTY PYTHON SIMULATIONS
# Define the number of simulations and initialize the counters for wins

num_simulations = int(input("How many simulations would you like to run on the monty hall python problem? "))
switch_wins = 0
stay_wins = 0

def monty_hall_problem():
    pass

# Print the results

