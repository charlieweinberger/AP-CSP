import random

def check_for_winner(input_board):

    # Get all possible combinations of 3

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

    # Check for a winner

    for row in all_combinations:
        if row[0] != "-" and row[0] == row[1] and row[1] == row[2]:
            if row[0] == "X":
                print("Player X wins!")
                exit()
            else:
                print("Player O wins!")
                exit()

    # Check for a tie

    if "-" not in input_board:
        print("Tie game!")
        exit()

# Run game

board = ["-", "-", "-", "-", "-", "-", "-", "-", "-"]

while True:

    # Prompt the user to choose a move

    print("You are player X.\n")

    print(board[0] + "|" + board[1] + "|" + board[2])
    print(board[3] + "|" + board[4] + "|" + board[5])
    print(board[6] + "|" + board[7] + "|" + board[8])

    print("\nWhere do you want to move? Input a number between 1 and 9.")

    # Execute the user's move

    move_index = int(input("Your move: ")) - 1
    board[move_index] = "X"

    # Check if the user has won

    check_for_winner(board)

    # Execute a random move

    available_moves = []
    for i in range(9):
        if board[i] == "-":
            available_moves.append(i)

    random_index = random.choice(available_moves)
    board[random_index] = "O"

    # Check if the user has lost

    check_for_winner(board)