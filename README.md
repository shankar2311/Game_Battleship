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


## Creating the Heroku app

When you create the app, you will need to add two buildpacks from the _Settings_ tab. The ordering is as follows:

1. `heroku/python`
2. `heroku/nodejs`

You must then create a _Config Var_ called `PORT`. Set this to `8000`

If you have credentials, such as in the Love Sandwiches project, you must create another _Config Var_ called `CREDS` and paste the JSON into the value field.

Connect your GitHub repository and deploy as normal.

## Constraints

The deployment terminal is set to 80 columns by 24 rows. That means that each line of text needs to be 80 characters or less otherwise it will be wrapped onto a second line.

-----
Happy coding!