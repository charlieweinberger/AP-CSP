class TicTacToe:
    
    def __init__(self):

        self.players = [1, 2]
        self.state = [[None for _ in range(3)] for _ in range(3)]
        self.winner = None

    def run_to_completion(self):
        
        print('\nWelcome to TicTacToe! \nExample of a move: 2,0 is the bottom left corner')

        while self.winner == None:
            self.complete_round()
        
        print(f'\nPlayer {self.winner} wins!')

    def complete_round(self):
        
        for player in self.players:
            
            player_move = self.choose_move(player)
            self.state[player_move[0]][player_move[1]] = player
            
            self.winner = self.check_for_winner()

            if self.winner:
                self.print_board()
                break

    def choose_move(self, player):
        
        choices = [[i, j] for i in range(3) for j in range(3) if self.state[i][j] == None]
        self.print_board()
        
        move = input(f'\nYou are player {player}\nYour move: ')
        choice = [int(elem) for elem in move if elem in '012']

        if choice not in choices:
            print('That move is not valid! Please try again.')
            return self.choose_move(player)
        
        return choice

    def check_for_winner(self):

        rcd = [
            [self.state[0][i] for i in range(3)],
            [self.state[1][i] for i in range(3)],
            [self.state[2][i] for i in range(3)],
            [self.state[i][0] for i in range(3)],
            [self.state[i][1] for i in range(3)],
            [self.state[i][2] for i in range(3)],
            [self.state[i][i] for i in range(3)],
            [self.state[i][2-i] for i in range(3)]
        ]

        board_full = True
        for row in rcd:
            
            if None in row:
                board_full = False

            for player in self.players:
                if row == [player for _ in range(3)]:
                    return player
        
        return 'tie' if board_full else None
  
    def print_board(self):

        print('')
        for row in self.state:
            row_string = ''
            for space in row:
                if space == None:
                    row_string += '_|'
                else:
                    row_string += str(space) + '|'
            print(row_string[:-1])

game = TicTacToe()
game.run_to_completion()