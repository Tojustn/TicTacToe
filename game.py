from player import HumanPlayer, RandomComputerPlayer, NaiveBacktrackingComputerPlayer
import time


class TicTacToe:
    def __init__(self):
        self.board = [' ' for _ in range(9)]
        self.current_winner = None
    
    # Prints current board with X's and O's
    def print_board(self):
        # This is getting the rows, i*3 this is the starting index: (i+1)*3 ending index, [0,3]; [3,6], [6,9]
        # The [self.board...] is the array that we are splicing 
        for row in [self.board[i*3:(i+1)*3] for i in range(3)]:
            # printing the 3x3 board, .join makes the middle item | O | then we are adding the other two lines to make vertical 3x3
            print('| ' + ' | '.join(row) + ' | ')

    # Prints 1-9 in board pattern
    @staticmethod # static because doesnt correspond to a specific board no self needed
    def print_board_nums():
        # 0 | 1 | 2 (tells us what number corresponds with each box)
        # the str(i) acts as a constructor making sure the numbers are a string
        # Basically its like for i in range(0,3) [0,1,2],[3,4,5]
        number_board = [[str(i) for i in range(j*3, (j+1)*3)] for j in range(3)]
        for row in number_board:
            print("| " + " | ".join(row) + " |")

    def avaliable_moves(self):
        moves = []
        # (i,spot) i is assigned the index of the tuple, x is the value uhsing enumerate
        for (i,spot) in enumerate(self.board):
            # x | o | x; (0,'x'), (1,'o'), (2,'x')
            if spot == ' ':
                moves.append(i)
        return moves

    # Checks if there are empty squares if not returns false
    def empty_squares(self):
        return " " in self.board

    # Returns number of empty squares
    def num_empty_squares(self):
        return len(avaliable_moves())

    # Checks if the move made was valid if not returns False
    def make_move(self,square,letter):
        # if valid move then make move
        # if not valid return False
        if self.board[square] == " ":
            self.board[square] = letter
            if self.winner(square, letter):
                self.current_winner = letter
            return True
        else:
            return False

    
    # Checks for the winner and change current_winner variable
    def tie(self):
        for value in self.board:
            if value == " ":
                return False
        return True
    def winner(self,square,letter):
        # Winner if 3 in a row anywhere
        # Gets row index divides by 3 and then rounds down 
        row_ind = square // 3
        # Gets array of string in the row
        row = self.board[row_ind*3: (row_ind+1)*3]
        # Uses all() Checks if all the values in row match each other
        if all(spot == letter for spot in row):
            return True4

        # Gets column index remainder of /3 
        col_ind = square % 3

        #Gets value in column, intervals of 3 because i*3, i will be 0+ind,3+ind,6+ind 
        column = [self.board[col_ind + i*3] for i in range(3)]
        if all(spot == letter for spot in column):
            return True

        # check diagonals 
        if square % 2 == 0:
            diagonal1 = [self.board[i] for i in [0,4,8]]
            diagonal2 = [self.board[i] for i in [2,4,8]]
            if all(spot == letter for spot in diagonal1 or diagonal2):
                return True
def play(game, x_player, o_player, print_game=True):
    if print_game:
        game.print_board_nums()
        time.sleep(.8)
    letter = "X"
    # while the game still has empty squares
    #just return winner
    while game.empty_squares():
        if letter == "O":
            square = o_player.get_move(game)
        else:
            square = x_player.get_move(game)

        if game.make_move(square, letter):
            if print_game:
                print(letter + f" makes a move to square {square}")
                game.print_board()
                print("")
                # return winner if there is one
                if game.current_winner:
                    if print_game:
                        print(letter + " wins!")
                    return letter

                # after make move alternate letter
                if letter == "X":
                    letter = "O"
                else:
                    letter = "X"
            # .8 second pause
            time.sleep(.8)
    if print_game:
        tie()
        print("TIE GAME")

if __name__ == "__main__":
    
    t = TicTacToe()
    x_player = HumanPlayer("X")
    o_player = NaiveBacktrackingComputerPlayer("O",t)
    play(t,x_player,o_player,True)