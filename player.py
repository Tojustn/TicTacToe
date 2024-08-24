import math
import random
class Player:
    def __init__(self,letter):
        # either x or o
        self.letter = letter
    def get_move(self,game):
        pass

class RandomComputerPlayer(Player):
    def __init__(self, letter):
        # Calls super() to make letter 
        super().__init__ (letter)
    def get_move(self,game):
        square = random.choice(game.avaliable_moves())
        return square


        
class NaiveBacktrackingComputerPlayer(Player):
    def __init__(self, letter,game):
        self.board = [' ' for _ in range(9)]
        # Calls super() to make letter 
        super().__init__ (letter)
        self.move_index = 0

    # Returns an optimal moveset
    
    def moveset(self,board):
            moves = self.recur_moveset([],board)
            # Checks wether moveset is a tie or a win
            if moves[0] == 1:
                return moves[1]
            if moves[0] == 2:
                 return moves[1]
           
    # Makes move on a simulated board
    def make_move(self,square,letter):
        # if valid move then make move
        # if not valid return False
        if self.board[square] == " ":
            self.board[square] = letter
            return True
        else:
            return False
    def tie(self,board):
        for value in board:
            if value == " ":
                return False
        return True

    def winner(self,square,letter,board):
        # Winner if 3 in a row anywhere
        # Gets row index divides by 3 and then rounds down 
        row_ind = square // 3
        # Gets array of string in the row
        row = board[row_ind*3: (row_ind+1)*3]
        # Uses all() Checks if all the values in row match each other
        if all(spot == letter for spot in row):
            return True

        # Gets column index remainder of /3 
        col_ind = square % 3

        #Gets value in column, intervals of 3 because i*3, i will be 0+ind,3+ind,6+ind 
        column = [board[col_ind + i*3] for i in range(3)]
        if all(spot == letter for spot in column):
            return True

        # check diagonals 
        if square % 2 == 0:
            diagonal1 = [board[i] for i in [0,4,8]]
            diagonal2 = [board[i] for i in [2,4,8]]
            if all(spot == letter for spot in diagonal1 or diagonal2):
                return True
    #Recursion function for the moveset
    def avaliable_moves(self,board):
        moves = []
        # (i,spot) i is assigned the index of the tuple, x is the value uhsing enumerate
        for (i,spot) in enumerate(board):
            # x | o | x; (0,'x'), (1,'o'), (2,'x')
            if spot == ' ':
                moves.append(i)
        return moves
    def recur_moveset(self,moves,board):
        
        # Algorithms move
        for i in self.avaliable_moves(board):
            self.make_move(i,"O")
            moves.append(i)
            if self.winner(i,"O",board): 
                return (1,moves)
            if self.tie(board):
                return (2,moves)
        # Simulates players move
        for i in self.avaliable_moves(board):
            self.make_move(i,"X")
            moves.append(i)
            if self.winner(i,"X",board): 
                return (0,moves)
            if self.tie(board):
                return (2,moves)
            else:
                return recur_moveset(moves)

    # Chooses an optimal moveset
    def get_move(self,game):
        self.board = game.board
        move = self.moveset(self.board)
        self.move_index = self.move_index + 1
        cur_move = self.move_index - 1
        return move[cur_move]

class HumanPlayer(Player):

    def __init__(self, letter):
        super().__init__(letter)
    def get_move(self,game):
        valid_square = False
        val = None
        while not valid_square:
            square = input(self.letter + "'s turn. Input move(0-9): ")
            try:
                val = int(square)
                if val not in game.avaliable_moves(): # checks if val is in game
                    raise ValueError # if not in val ValueError is raised
                valid_square = True
            except ValueError:
                print("That was not a valid move. Try again")

        return val
    