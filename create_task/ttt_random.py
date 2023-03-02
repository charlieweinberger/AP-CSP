import random

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

board = ["-", "-", "-", "-", "-", "-", "-", "-", "-"]
winner = None

print("You are player X.")

while winner == None:
            
    print_board(board)
    print("Where do you want to move? Input a number between 1 and 9.")

    move_index = int(input("Your move: ")) - 1
    
    if 0 <= move_index <= 8 and board[move_index] == "-":
        board[move_index] = "X"
    else:
        print("Invalid move!")
    
    winner = check_for_winner(board)
    
    if winner == None:
        
        available_moves = []
        for i in range(9):
            if board[i] == "-":
                available_moves.append(i)

        random_index = random.choice(available_moves)
        board[random_index] = "O"
        winner = check_for_winner(board)

print_board(board)

if winner == "X":
    print("You win!")
else:
    print("You lose!")