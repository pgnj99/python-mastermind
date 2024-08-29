from play import *
from options import *

print('MASTERMIND')
print('1: Classic')
print('2: Puzzle')
print('3: Options')

check = False

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
        classic(int(total), int(given))
    #elif choice == "2":
        #play(2)
    elif choice == "3":
        options()
    elif choice == "0":
        print("Thank you for playing!")
        break
    else:
        print("Invalid choice.")