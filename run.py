from random import randint

player_name = input("Please enter your name:")

class Board:
    """
    Main board class. Sets board size.
    Has methods for printing board for both player and computer.
    code inspired from Code Institute lessons
    """
    def __init__(self):
        self.board = [["."] * 5 for i in range(5)]

    #Below code is taken from Code Institute project portfolio
    def print_board(self):
        for row in self.board:
            print(" ".join(row))

  
class Ship:
    """
    The ship class places a ship at a random location on the board.
    
    """
    def __init__(self, board):
        self.board = board
        self.ship_row = randint(0, len(self.board.board) - 1) 
        self.ship_col = randint(0, len(self.board.board) - 1) 


class StartGame:
    """
    In StartGame class allows the player to guess the location of the ship.
    """
    def __init__(self):
        self.board = Board()
        self.ship = Ship(self.board) 

    def make_guess(self):
        x = int(input("Guess a row:"))
        y = int(input("Guess a column:"))
        return (x, y) 

