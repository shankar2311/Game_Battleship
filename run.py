from random import randint

class Board:
    """
    Main board class. Sets board size.
    Has methods for printing board for both player and computer.
    code inspired from Code Institute lessons
    """
    #Variable to store hit points
    score = 0

    def __init__(self, name):
        self.name = name
        self.board = [["."] * 5 for i in range(5)]
        self.ship_locations = []
        self.add_ships()
        

    def add_ships(self):
        """
        In this method we add 4 ships to both player board and computer board
        Ships in player board are visible and ships in computer board are not shown.
        code is inspired from Code Institute lessons and from youtube.
        """
        p = 0 

        if self.name != "computer":

            while p < 4:
                row = randint(0, len(self.board) - 1)
                col = randint(0, len(self.board[0]) - 1)
                if self.board[row][col] != "@":
                    self.board[row][col] = "@"
                    self.ship_locations.append((row, col))
                    p = p+1
                   
        else:

            while p < 4:
                row = randint(0, len(self.board) - 1)
                col = randint(0, len(self.board[0]) - 1)
                if (row, col) not in self.ship_locations:
                    self.ship_locations.append((row, col))
                    p = p+1
                    
            
    #Below code is taken from Code Institute project portfolio
    def print_board(self):
        print("\n"+self.name+"'s board \n")
        for row in self.board:
            print(" ".join(row))

    def player_guess(self):
        """
        Code inspired from Code Institute lessons and challenges
        """

        while True:
            try:
                row = int(input("Guess a row(0-4) :\n"))
                col = int(input("Guess a column(0-4) :\n"))
            except ValueError:
                print("You must enter an integer") 
                continue 

            if (row >4 and col > 4):
                print("Your guess is out of range! Try again..\n")
            else:
                return (row, col)

                

    def computer_guess(self):
        print("computer is guessing now..\n")
        row = randint(0, 4)
        col = randint(0, 4)

        return (row, col)


    def check_guess(self, row_col, opp_player):
        """
        Takes first argument as tuple and second argument as Board object.
        Check's whether player guess and computer guess hit a ship or not.
        And scores of each player and computer are updated accordingly.
        Code inspired from other battleship game you tube videos.
        """
        if row_col in opp_player.ship_locations:
            self.score = self.score + 1
            print("Hit Successful!. "+self.name+"'s score is ",self.score) 
            
            opp_player.board[row_col[0]][row_col[1]] = "X"
        else:
            print("\n"+self.name+"'s hit unsuccessful\n")
            opp_player.board[row_col[0]][row_col[1]] = "O" 


    def new_game():
        """
        Starts new game and prints information about the battleship game
        """
        print("_" * 35)
        print("\nwelcome to BATTLESHIP GAME!!\n")
        print("Board size : 5. Number of Ships : 4\n")
        print("Top left corner is row : 0, col : 0\n")
        print("'@' = Player ship location\n")
        print("'X' = Hit\n")
        print("'O' = Miss\n")
        print("_" * 35)
        print("\n\n Let's Play\n\n")


        #Initiates playerboard and prints the board for the player
        player = Board(input("Please enter player name:"))
        player.print_board()

        #Initiates computerboard and prints the board for the computer
        computer = Board("computer")
        computer.print_board()
        
        """
        Code is inspired from other battleship game's code.

        Check the guesses of both player and computer, raises error
        messsage if same row and column is already used.

        And displays who the winner is after the game.
        """

    
        while player.score < 4 and computer.score < 4:

            while True:
                p_row_col = player.player_guess()

                if computer.board[p_row_col[0]][p_row_col[1]] not in ['X', 'O']:

                    player.check_guess(p_row_col, computer)
                    computer.print_board()
                    break
                else:
                    print("Coordinates already used\n") 


            while True:
                c_row_col = computer.computer_guess()

                if player.board[p_row_col[0]][p_row_col[1]] not in ['X', 'O']:

                    computer.check_guess(p_row_col, player)
                    player.print_board()
                    break
                else:
                    print("Coordinates already used\n") 

        if player.score > computer.score:
            print("\nCongratulations You won!!\n")
        else:
            print("\nComputer won!!\n")        

        
Board.new_game()    
