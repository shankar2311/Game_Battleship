# BATTLESHIP GAMEB

Battleship game is python terminal game, Which runs in the Code institute mock terminal on Heroku.

Users can try to beat the computer by finding all of the computer's battleships before the computer finds theirs. Each battleship occupies one square on the board.

Welcome!

## How to play

* Battleship game is based on the classic pen-and-paper game.
* You can read more about it on Wikipedia.
* In this game the size of the board is 5 by 5 matrix and number of ships are 4.
* The player can see where their ships are, indicated by an @ sign here is 4, but cannot see where the computer ship's are.
* Guesses are marked on the board by 'O'. Hits are marked by 'X'.
* The player and the computer then take it in turns to make guesses and try to sink each other's battleships.
* The winner is the player who sinks all of their opponent's battleships first.


## Features

### Existing Features

* Random board generation
  - Ships are  randomly placed on both the player and computer board
  - THe player cannot see where the computer's board are


  - Play against the computer
  - Accepts user input
  - Maintain scores
* Input validation and error checking
  - You cannot enter coordinates outside of the grid
  - You must enter numbers
  - You cannot enter same guess twice
  - Data maintained in class instances

### Future Features  
  - Allow player to select the board size and number of ships
  - Allow player to position ships themselves
  - Have ships larger than 1x1

## Data Model

I decided to use a Board class as my model. The game creates two instances of the board class to hold the player's and computer's board.

The Board class has methods to help play the game, such as print method to print out the current board, an add_ships method to add ships to the board, player_guess method for player to guess, computer_guess method for computer to guess, check_guess method to validate guesses and new_game method to play the game and return the results

## Testing

I have manually tested this project by doing the following:

* Passed the code through a PEP8 linter and found some errors.
* Given invalid inputs: strings when numbers are expected, out of bounds inputs, same input twice.
* Tested in my local terminal and the Code institute Heroku terminal

## Bugs
### Solved Bugs

* Getting error if we press any key without entering the values or by entering string, so i fixed it by adding try except statements

### Remaining Bugs
* Unknown

### Validator Testing
* PEP8
  - Some errors were returned from PEP8online.com

### Deployment

This project was deployed using Code institutes's mock terminal for Heroku

* Steps for deployement
  - Fork or clone this respository
  - Create a new Heroku app
  - Set the Buildbacks to python and NodeJS in that order
  - Link the Heroku app to the repository
  - Click on Deploy

### Credits
* Code Institute for the deployement terminal
* Basic idea of the game is taken from Code institutes project portfolio 3 
* Code is mostly inspired from other battleship game videos from youtube and chatgpt
* Used Jupyter notebook for debugging code step by step 

### Acknowledgement
* Very thankfull to my mentor rory_patrick for valuable suggestions
* Thankfull to Code institutes Slack Community







