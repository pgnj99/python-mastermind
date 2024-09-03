# Python Master Mind

A Python adaptation of the paper & pencil game codebreaker, also known by the board game adaptation Master Mind. Enter a sequence of characters to guess the secret "code" based on the available marks.

Developed to practice and further explore Python concepts. Utilizes modules, input validation, inheritance, polymorphism, file access, and ANSI color codes.

Run main.py to start game.

## Features
* A classic-styled game mode in which player can make limited amount of guesses recorded on game board.
* A puzzle-styled game mode inspired by online adaptations in which player must use pre-set clues to determine code.
* Customizable peg numbers for classic game and difficulty options for puzzle game.
* Detailed in-game instructions for each game mode.
* Options menu to enable colored pegs, change mark symbols, or toggle repeatable colors on board.
* File creation and management to retain settings across multiple play sessions.

## Options file
Upon starting the program for the first time, an options.txt file is automatically created in the program directory containing the player's game settings. The file is formatted with three lines:
1. Integer for peg color settings (0 - Colorless; 1 - Colored Text; 2 - Colored Backgrounds)
2. Three characters representing mark symbols for correct position (●), incorrect position (◌), and incorrect peg (·), in that order
3. Integer to toggle repeatable colors (0 - OFF; 1 - ON)

Once automatically created, the options.txt file will be retrieved, allowing settings to persist between program sessions. To prevent errors during gameplay, the program will detect if the file is formatted incorrectly and prompt the user to either restore default settings or exit the program.m.
