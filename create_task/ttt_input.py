def check_for_winner(input_board):

    all_combinations = [
        [input_board[0], input_board[1], input_board[2]],
        [input_board[3], input_board[4], input_board[5]],
        [input_board[6], input_board[7], input_board[8]],
        [input_board[0], input_board[3], input_board[6]],
        [input_board[1], input_board[4], input_board[7]],
        [input_board[2], input_board[5], input_board[8]],
        [input_board[0], input_board[4], input_board[8]],
        [input_board[2], input_board[4], input_board[6]]
    ]

    for row in all_combinations:
        if row[0] != "-" and len(set(row)) == 1:
            return row[0]

    if "-" in input_board:
        return None
    else:
        return "tie"

def print_board(input_board):
    print("")
    print(f"{input_board[0]}|{input_board[1]}|{input_board[2]}")
    print(f"{input_board[3]}|{input_board[4]}|{input_board[5]}")
    print(f"{input_board[6]}|{input_board[7]}|{input_board[8]}")
    print("")

players = ["X", "O"]
board = ["-", "-", "-", "-", "-", "-", "-", "-", "-"]
winner = None

while winner == None:
    
    for player in players:
        
        print_board(board)
        print(f"You are player {player}.")
        print("Where do you want to move? Input a number between 1 and 9.")

        move_index = int(input(f"Your move: ")) - 1
        
        if 0 <= move_index <= 8 and board[move_index] == "-":
            board[move_index] = player
        else:
            print("Invalid move!")
        
        winner = check_for_winner(board)
        if winner: break

print_board(board)
print(f"Player {winner} wins!")