from time import time
from codemaker import *

def guess_list(code, guess):
    guesslist = []
    for peg in guess:
        if peg.isalpha():
            guesslist.append(peg.upper())
            
    if len(guesslist) != len(code.get_code()):
        print("Invalid guess. Try again.")
        return None
    else:
        return guesslist

def get_time(start, end):
    total = int(end - start)
    minutes = total // 60
    seconds = total - (minutes * 60)
    
    if minutes > 0:
        return str(minutes) + " minutes, " + str(seconds) + " seconds"
    else:
        return str(seconds) + " seconds"

def classic(total, given, settings):
    code = ClassicGame(total, given, settings)
    chances = code.guesses
    guesses = 0
    start_time = time()

    while True:
        print()
        code.display_table()
        if chances == guesses:
            print("Sorry, you've run out of guesses!")
            print("The correct code:")
            code.display_code()
            break
        print("You have " + str(chances - guesses) + " guesses remaining.\n")
        code.list_colors()

        guess = input("Make your guess here: ")
        print()
        if guess == '0':
            break
        
        guess = guess_list(code, guess)
        if guess == None:
            continue

        if code.check(guess):
            end_time = time()
            code.display_table()
            print("You win!")
            print("Completed in " + get_time(start_time, end_time) + "\n")
            break
        guesses += 1

def puzzle(total, given, count, settings):
    code = PuzzleGame(total, given, count, settings)
    start_time = time()

    while True:
        print()
        code.display_clues()
        code.list_colors()

        guess = input("Make your guess here: ")
        print()
        if guess == '0':
            break

        guess = guess_list(code, guess)
        if guess == None:
            continue

        if code.compare(guess):
            end_time = time()
            print("You win!")
            print("Completed in " + get_time(start_time, end_time) + "\n")
            break