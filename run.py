from random import randint



class Board:
    """
    Main board class. Sets board size.
    Has methods for printing board for both player and computer.
    code inspired from Code Institute lessons
    """

    score = 0

    def __init__(self):

        self.board = [["."] * 5 for i in range(5)]
        self.ship_locations = []

    #Below code is taken from Code Institute project portfolio
    def print_board(self):

        for row in self.board:
            print(" ".join(row))

    def add_ships_player(self):
        """
        In this method we add 3 ships to both player board and computer board
        Ships in player board are visible and ships in computer board are invisible
        """
        for i in range(3):
            row = randint(0, len(self.board) - 1)
            col = randint(0, len(self.board[0]) - 1)
            if self.board[row][col] != "@":
                self.board[row][col] = "@"
                self.ship_locations.append((row, col))
            else:
                print("Error: You cannot add more ships") 

    def add_ships_computer(self):          

        for i in range(3):
            row = randint(0, len(self.board) - 1)
            col = randint(0, len(self.board[0]) - 1)
            if (row, col) not in self.ship_locations:
                pass
            else:
                self.ship_locations.append((row, col))
            


    def player_guess(self):

        while True:
            try:
                row = int(input("Guess a row(0-4):"))
                col = int(input("Guess a column(0-4):"))

                if (row < 4 and col < 4):
                    raise ValueError("Your guess is out of range!")

                return (row, col)

            except ValueError as e:
                print(e)    

    def computer_guess(self):

        row = randint(0, 4)
        col = randint(0, 4)

        return (row, col)


    def check_guess(self, row_col, opp_player):
        """
        Takes first argument as tuple and second argument as Board object.
        Check's whether player guess and computer guess hit a ship or not.
        And scores of each player and computer are updated accordingly.
        """
        if row_col in opp_player.ship_locations():
            self.score = self.score + 1
            print("Hit Successful!") 
            
            opp_player.board[row_col[0]][row_col[1]] = "X"
        else:
            print("Hit Unsuccessful")
            opp_player.board[row_col[0]][row_col[1]] = "O"     


    




player = Board()
computer = Board()

player.add_ships_player()
player.print_board()

computer.add_ships_computer()
computer.print_board()
