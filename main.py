import os
from sys import exit
from play import *
from options import *

print('MASTERMIND')
print('1: Classic')
print('2: Puzzle')
print('3: Options')
print('4: Instructions')

settings = [0, ["●", "◌", "·"], True]

if not os.path.exists("options.txt"):
    make_file()

settings = get_settings()
if settings == False:
    print("options.txt file is unreadable. Please delete file to continue.")
    exit(1)

# This loop will run for as long as the player wants to continue playing
while True:
    choice = input('Enter a number to select your mode or enter 0 to exit. ')

    if choice == "1":
        while True:
            total = input('How many pegs would you like to use? Enter a number between 3 and 7. ')
            if total.isnumeric() and 3 <= int(total) <= 7:
                break
            else:
                print('Invalid count.')
        while True:
            given = input('How many peg colors would you like to be available? Enter a number between 3 and 7. ')
            if not settings[2] and given < total:
                print('Repeat colors is turned off, and you cannot have fewer peg colors than pegs (' + total + ').')
            elif given.isnumeric() and 3 <= int(given) <= 7:
                break
            else:
                print('Invalid count.')
        classic(int(total), int(given), settings)

    elif choice == "2":
        print("Select a difficulty:")
        print("1. Easy (3 pegs)")
        print("2. Medium (4 pegs)")
        print("3. Hard (5 pegs)")
        choice = input()
        while True:
            if choice.isnumeric():
                if int(choice) == 1:
                    puzzle(3, 3, 3, settings)
                elif int(choice) == 2:
                    puzzle(4, 4, 4, settings)
                elif int(choice) == 3:
                    puzzle(5, 5, 5, settings)
                else:
                    choice = input('Invalid choice, try again: ')

    elif choice == "3":
        settings = options(settings)

    elif choice == "4":
        print("\n")
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
        
        print("3: Options")
        print("Configure certain settings related to the game.\n")
        print("'Peg colors' allows you to apply colored text or backgrounds to each peg based on their symbol. Note that colors may not display properly depending on your system and settings.\n")
        print("'Mark symbols' allows you to change any of the three mark symbols to one of your choice.\n")
        print("'Repeat colors' will set whether a code can consist of multiple pegs of the same color. Whatever it's set to, you're still allowed to guess repeat colors.\n")
        print("Your settings are saved across sessions to a text file, options.txt. Be careful when editing this file, as the game will be unable to run if it is not formatted correctly.\n")
        
        print("\n")
        print("Enter 0 at any point during gameplay to return to the menu. Have fun!\n")

    elif choice == "0":
        print("Thank you for playing!")
        break
    else:
        print("Invalid choice.")