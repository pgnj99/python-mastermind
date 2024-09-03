# Mastermind by Peter Giordano
# Developed in August 2024

import os
import random
from sys import exit
from play import *
from options import *

# Title is printed here
print('\nMASTERMIND\n')

# Settings is used to customize certain aspects of gameplay
# In order, list elements determine color settings, mark symbols, and repeat colors

# Settings are stored in file on computer in order to persist between game sessions
# If file does not exist, it will automatically be created
if not os.path.exists("options.txt"):
    make_file()

# If file exists, settings will be retrieved from contents
settings = get_settings()

# Program cannot be run if file is improperly formatted for gameplay
# User will be prompted to either restore default settings or exit program
if settings == False:
    restore = input("options.txt file is unreadable. Enter Y to restore default settings, or a different key to exit program: ")
    if restore == "Y":
        make_file()
        settings = get_settings()
    else:
        exit(1)

# This loop will run for as long as the player wants to continue playing
while True:
    print('1: Classic')
    print('2: Puzzle')
    print('3: Options')
    print('4: Instructions')
    choice = input('Enter a number to select your mode or enter 0 to exit. ')
    print()

    # 1: Classic
    if choice == "1":
        # User will be able to select number of pegs and colors
        # Input validation is used to check for numeric values
        while True:
            total = input('How many pegs (3 - 7) would you like to use? ')
            if total.isnumeric() and 3 <= int(total) <= 7:
                break
            else:
                print('Invalid count.\n')
        while True:
            given = input('How many peg colors (3 - 7) would you like to be available? ')

            # With repeat colors turned off, having more peg colors than pegs will be impossible
            if given.isnumeric() and not settings[2] and int(given) < int(total):
                print('Repeat colors is turned off, and you cannot have fewer peg colors than pegs (' + total + ').\n')
            elif given.isnumeric() and 3 <= int(given) <= 7:
                break
            else:
                print('Invalid count.\n')
        while True:
            classic(int(total), int(given), settings)

            # Upon game end or exit, player can choose to replay with same settings
            replay = input("Enter Y to play a new puzzle, or a different key to return to menu. ")
            print()
            if replay.upper() != 'Y':
                break

    # 2: Puzzle
    elif choice == "2":
        # Premade difficulties determine numbers of pegs, colors, and clues
        print("Select a difficulty:")
        print("1. Easy (3 pegs)")
        print("2. Medium (4 pegs)")
        print("3. Hard (5 pegs)")
        print("4. Monster (7 pegs, hex shape, matching colors cannot touch)")
        num = ['3', '4', '5', '7']
        choice = input()
        while True:
            if choice.isnumeric() and 0 < int(choice) <= 4:
                break
            else:
                choice = input('Invalid choice, try again: ')
        
        # Number of colors may randomly change between difficulties
        # With repeat colors turned off, color counts fewer than peg counts must not be made available
        while True:
            if int(choice) == 1:
                puzzle(3, random.choice([3,4]), 3, settings)
            elif int(choice) == 2:
                puzzle(4, random.choice([4,5]), 4, settings)
            elif int(choice) == 3:
                if settings[2]:
                    puzzle(5, random.choice([4,5]), 5, settings)
                else:
                    puzzle(5, 5, 5, settings)
            elif int(choice) == 4:
                if settings[2]:
                    puzzle(7, random.choice([5,6,7]), 6, settings)
                else:
                    puzzle(7, 7, 6, settings)
                
            # Upon game end or exit, player can choose to replay with same settings
            replay = input("Enter Y to play a new puzzle, or a different key to return to menu. ")
            print()
            if replay.upper() != 'Y':
                break

    # 3: Options
    elif choice == "3":
        settings = options(settings)

    # 4: Instructions
    elif choice == "4":
        print("INSTRUCTIONS")
        print("Mastermind, also known as Codebreaker, is a tabletop game in which one player (the code maker) makes a 'code', which is a collection of colored pegs, and the second player (the code breaker) must guess the code.\n")
        print("You will play as the code breaker. Each peg color is represented by a letter, and you must enter the full sequence of letter to make your guess. Guess the correct sequence of letters and you win!\n")
        
        print("1: Classic")
        print("The classic game of Mastermind, as the name suggests. Each guess wll fill up a slot on the board, and you have a limited number of guesses before filling it up completely. Fill the board before guessing the correct code and you lose!\n")
        print("Each guess will be given a special marking to indicate how close your guess was to the correct code. The following marks will appear:\n")
        print(settings[1][0] + ": You have a peg in the correct position.")
        print(settings[1][1] + ": You have a peg that appears in the code, but it's in the wrong position.")
        print(settings[1][2] + ": You have a peg that does not appear in the code.")
        print("A correct guess will have a " + settings[1][0] + " filling each slot. There's all sorts of logical tricks you can employ based on your marks, so study each guess carefully!\n")
        
        print("2: Puzzle")
        print("A differently structured take on the original game. There is no more board, and your guesses will not be recorded or marked. Instead, a preset selection of guesses will be laid out to you, each having their own marks. You must guess the code based on these clues.\n")
        print("Your guess will be compared to each clue, and it will fail it conflicts with a clue's marks. The secret to this game? The marks on each clue are the marks your guess should have when compared to each clue.\n")
        print("You're not limited with how many guesses you can make, so guess as many times as you'd like!\n")
        print("Looking for a vile challenge? Beware the Monster difficulty! Seven pegs are arranged in a hexagonal grid where matching colors cannot touch. This means one color can appear up to three times, and the middle color can only appear once!\n")
        
        print("3: Options")
        print("Configure certain settings related to the game.\n")
        print("'Peg colors' allows you to apply colored text or backgrounds to each peg based on their symbol. Note that colors may not display properly depending on your system and settings.\n")
        print("'Mark symbols' allows you to change any of the three mark symbols to one of your choice.\n")
        print("'Repeat colors' will set whether a code can consist of multiple pegs of the same color. Whatever it's set to, you're still allowed to guess repeat colors.\n")
        print("Your settings are saved across sessions to a text file, options.txt. Be careful when editing this file, as the game will be unable to run if it is not formatted correctly.\n")
        
        print("\n")
        print("Enter 0 at any point during gameplay to return to the menu. Have fun!\n")

    # Program will end if 0 is entered
    elif choice == "0":
        print("Thank you for playing!\n")
        break
    else:
        print("Invalid choice.\n")