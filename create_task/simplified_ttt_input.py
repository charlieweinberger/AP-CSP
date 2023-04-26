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

    for combination in all_combinations:
        if combination[0] == "X" and combination[1] == "X" and combination[2] == "X":
            return "Player X wins!"
        elif combination[0] == "O" and combination[1] == "O" and combination[2] == "O":
            return "Player O wins!"

    # Check for a tie

    if "-" not in input_board:
        return "Tie game!"
    
    return None

# Run game

board = ["-", "-", "-", "-", "-", "-", "-", "-", "-"]

while True:

    for player in ["X", "O"]:

        print("You are player " + player + ".")
        
        print(board[0] + "|" + board[1] + "|" + board[2])
        print(board[3] + "|" + board[4] + "|" + board[5])
        print(board[6] + "|" + board[7] + "|" + board[8])
       
        print("Where do you want to move? Input a number between 1 and 9.")

        move_index = int(input("Your move: ")) - 1
        board[move_index] = player

        winner = check_for_winner(board)
        
        if winner != None:
            print(board[0] + "|" + board[1] + "|" + board[2])
            print(board[3] + "|" + board[4] + "|" + board[5])
            print(board[6] + "|" + board[7] + "|" + board[8])
            print(winner)
            exit()