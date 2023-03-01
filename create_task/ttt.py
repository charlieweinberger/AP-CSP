def check_for_winner():

    all_combinations = [
        [board[0], board[1], board[2]],
        [board[3], board[4], board[5]],
        [board[6], board[7], board[8]],
        [board[0], board[3], board[6]],
        [board[1], board[4], board[7]],
        [board[2], board[5], board[8]],
        [board[0], board[4], board[8]],
        [board[2], board[4], board[6]]
    ]

    for row in all_combinations:
        if row[0] != "-" and len(set(row)) == 1:
            return row[0]
    
    if all([elem != "-" for elem in board]):
        return "tie"
    else:
        return None

players = ["X", "O"]
board = ["-" for _ in range(9)]
winner = None

while winner == None:
    
    for player in players:
        
        print("")
        print(f"{board[0]}|{board[1]}|{board[2]}")
        print(f"{board[3]}|{board[4]}|{board[5]}")
        print(f"{board[6]}|{board[7]}|{board[8]}")
        print("")
        print(f"You are player {player}.")
        print("Where do you want to move? Input a number between 1 and 9.")

        move_index = int(input(f"Your move: ")) - 1
        
        if 0 <= move_index <= 8 and board[move_index] == "-":
            board[move_index] = player
        else:
            print("Invalid move!")
        
        winner = check_for_winner()
        if winner: break

print("")
print(f"{board[0]}|{board[1]}|{board[2]}")
print(f"{board[3]}|{board[4]}|{board[5]}")
print(f"{board[6]}|{board[7]}|{board[8]}")
print("")
print(f"Player {winner} wins!")