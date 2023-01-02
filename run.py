# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
player_name = input("Please enter your name:")
size = 5
num_ships = 4

class Board:
    """
    Main board class. Sets board size, the number of ships,
    the player's name and the board type (player or computer).
    code taken from Code Institute's Project Portfolio
    """
    def __init__(self, size, num_ships, name, type):
        self.size = size
        self.num_ships = num_ships
        self.name = name
        self.type = type
        self.board = [["." for x in range(size)] for y in range(size)]
        self.guesses = []

    def display_board(self):
        """
        Displays the board
        code taken from Code Institute's Project Portfolio
        """
        
        for row in self.board:
            print(" ".join(row))

    def guess_attack(self, x, y):
        """
        Guesses the given coordinates that entered by player
        hits the computer's ships or not and stores in guesses list.
        And also computer guesses
        code inspired from Code Institute's Project Portfolio
        """
        self.guesses.append((x, y))
        self.board[x][y] = "X"
        if (x, y) in self.ships:
            self.board[x][y] = "*"
            return "Hit"
        else:
            return "Miss"    
            
              


computer_board = Board(size, num_ships, "computer", type="computer")
player_board = Board(size, num_ships, "player_name", type="player")
name = player_name
print(f"{name} board")
print(player_board.display_board())
print("computer board")
print(computer_board.display_board())
        