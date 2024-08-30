import os
from sys import exit
from play import *
from options import *

print('MASTERMIND')
print('1: Classic')
print('2: Puzzle')
print('3: Options')

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
            if given.isnumeric() and 3 <= int(given) <= 7:
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
    elif choice == "0":
        print("Thank you for playing!")
        break
    else:
        print("Invalid choice.")