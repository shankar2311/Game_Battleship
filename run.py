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

    def add_ships(self):
        """
        In this method we add 3 ships to both player board and computer board
        Ships in player board are visible and ships in computer board are invisible
        """
        for i in range(3):
            row = randint(0, len(self.board) - 1)
            col = randint(0, len(self.board[0]) - 1)
            if self.board[row][col] != "@":
                self.board[row][col] = "@"
            else:
                print("Error: You cannot add more ships")    


        


  
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
    In StartGame class allows the player and computer to guess the location of the ship.
    """
    def __init__(self):

        self.board = Board()
        self.ship = Ship(self.board) 


    def make_guess(self):

        while True:
            try:
                x = int(input("Guess a row(0-4):"))
                y = int(input("Guess a column(0-4):"))

                if x < 0 or x > 4 or y < 0 or y > 4:
                    raise ValueError("Your guess is out of range!")

                return (x, y)

            except ValueError as e:
                print(e)    

    def computer_guess(self):

        x = randint(0, 4)
        y = randint(0, 4)

        return (x, y)


    def check_winner(self, x, y):
        # Checks the winner, returns true if all the ships have been hit otherwise returns false
        if x == self.ship.ship_row and y == self.ship.ship_col:
            return True
        else:
            return False       


player = Board()
player.add_ships()
print(player.board)
player.print_board()
