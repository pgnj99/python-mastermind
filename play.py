from time import time
from codemaker import *

# Guess strings will be converted to lists to be compared with code
def guess_list(code, guess):
    guesslist = []

    # Only characters representing active pegs will be added to list
    for peg in guess:
        if peg in code.get_code(code.colors):
            guesslist.append(peg.upper())
    
    # Guess will fail if resulting list is not the same size as code
    # Invalid guesses will not be counted or checked
    if len(guesslist) != len(code.get_code()):
        print("Invalid guess. Try again.")
        return None
    else:
        return guesslist

# Time to solve puzzle will be recorded and revealed at end of game
def get_time(start, end):
    total = int(end - start)
    minutes = total // 60
    seconds = total - (minutes * 60)
    
    # Display time in minutes (if applicable) and seconds
    if minutes > 0:
        return str(minutes) + " minutes, " + str(seconds) + " seconds"
    else:
        return str(seconds) + " seconds"

# Classic game
def classic(total, given, settings):
    # Define code object, maximum guesses, number of guesses, and starting time
    code = ClassicGame(total, given, settings)
    chances = code.guesses
    guesses = 0
    start_time = time()

    # Play loop
    while True:
        print()
        # Table will be displayed with new guesses inserted on every loop
        code.display_table()

        # Game will end if player reaches limit of guesses
        if chances == guesses:
            print("Sorry, you've run out of guesses!")
            print("The correct code:")
            code.display_code()
            break

        # Display remaining guesses and available peg colors
        print("You have " + str(chances - guesses) + " guesses remaining.\n")
        code.list_colors()

        guess = input("Make your guess here: ")
        print()

        # Player can exit game at any point by entering 0
        if guess == '0':
            break
        
        guess = guess_list(code, guess)
        if guess == None:
            continue

        # Game will end if player correctly guesses code
        if code.check(guess):
            end_time = time()
            code.display_table()
            print("\nYou win!")
            print("Completed in " + get_time(start_time, end_time) + "\n")
            break

        # Increment for each failed guess
        guesses += 1

# Puzzle game
def puzzle(total, given, count, settings):
    # Define code object and starting time
    code = PuzzleGame(total, given, count, settings)
    start_time = time()

    # Play loop
    while True:
        print()
        # Clues and peg colors will be displayed on every loop
        code.display_clues()
        code.list_colors()

        guess = input("Make your guess here: ")
        print()

        # Player can exit game at any point by entering 0
        if guess == '0':
            break

        guess = guess_list(code, guess)
        if guess == None:
            continue

        # Game will end if player correctly guesses code
        if code.compare(guess):
            end_time = time()
            print("\nYou win!")
            print("Completed in " + get_time(start_time, end_time) + "\n")
            break