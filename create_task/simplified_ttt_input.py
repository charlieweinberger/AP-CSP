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
            return row[0]

    # Check for a tie

    if "-" not in input_board:
        return "tie"
    else:
        return None

# Run game

board = ["-", "-", "-", "-", "-", "-", "-", "-", "-"]

while True:

    # Loop through each player

    for player in ["X", "O"]:

        # Prompt the player to choose a move

        print("You are player " + player + ".\n")

        print(board[0] + "|" + board[1] + "|" + board[2])
        print(board[3] + "|" + board[4] + "|" + board[5])
        print(board[6] + "|" + board[7] + "|" + board[8])

        print("\nWhere do you want to move? Input a number between 1 and 9.")

        # Execute the player's move

        move_index = int(input("Your move: ")) - 1
        board[move_index] = player

        # Check for a winner

        winner = check_for_winner(board)

        if winner == player:
            print("Player " + player + " wins!")
        elif winner == "tie":
            print("Tie game!")