from random import randint



class Board:
    """
    Main board class. Sets board size.
    Has methods for printing board for both player and computer.
    code inspired from Code Institute lessons
    """

    score = 0

    def __init__(self, name):
        self.name = name
        self.board = [["."] * 5 for i in range(5)]
        self.ship_locations = []
        

    #Below code is taken from Code Institute project portfolio
    def print_board(self):

        for row in self.board:
            print(" ".join(row))

    def add_ships(self):
        """
        In this method we add 3 ships to both player board and computer board
        Ships in player board are visible and ships in computer board are invisible
        """
        p = 0 

        if self.name != "computer":

            for i in range(3):
                while p < 3:
                    row = randint(0, len(self.board) - 1)
                    col = randint(0, len(self.board[0]) - 1)
                    if self.board[row][col] != "@":
                        self.board[row][col] = "@"
                        self.ship_locations.append((row, col))
                        p = p+1
                        break
        else:

            for i in range(3):
                while p < 3:
                    row = randint(0, len(self.board) - 1)
                    col = randint(0, len(self.board[0]) - 1)
                    if (row, col) not in self.ship_locations:
                        self.ship_locations.append((row, col))
                        p = p+1
                        break
            


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
            opp_player.board[row_col[0]][row_col[1]] = "o"     


    
    def new_game():
        """
        Starts new game and prints information about the battleship game
        """
        print("_" * 35)
        print("welcome to BATTLESHIP GAME!!")
        print(f"Board size : 5. Number of Ships : 3")
        print("Top left corner is row : 0, col : 0")
        print("'@' = Player ship location")
        print("'X' = Hit ")
        print("'o' = Miss")
        print("_" * 35)
        print("\n\n Let's Play\n\n")
        
#Initiates playerboard and prints the board for the player
player = Board(input("Please enter player name:"))
player.print_board()

#Initiates computerboard and prints the board for the computer
computer = Board("computer")
computer.print_board()

        

    
