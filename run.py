from random import randint

player_name = input("Please enter your name:")

class Board:
    """
    Main board class. Sets board size.
    Has methods for printing board for both player and computer
    code inspired from Code Institute lessons
    """
    def __init__(self):
        self.board = [["."] * 5 for i in range(5)]

    #Below code is taken from Code Institute project portfolio
    def print_board(self):
        for row in self.board:
            print(" ".join(row))
  