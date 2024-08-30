from codemaker import *

def guess_list(code, guess):
    guesslist = []
    while True:
            for peg in guess:
                if peg.isalpha():
                    guesslist.append(peg.upper())
            
            if len(guesslist) != len(code.get_code()):
                guess = input("Invalid guess. Try again: ")
                guesslist = []
            else:
                return guesslist

def classic(total, given, settings):
    code = ClassicGame(total, given, settings)
    chances = code.guesses
    guesses = 0

    while True:
        code.display_table()
        if chances == guesses:
            print("Sorry, you've run out of guesses!")
            print("The correct code:")
            code.display_code()
            break
        print("You have " + str(chances - guesses) + " guesses remaining.")
        code.list_colors()

        guess = input("Make your guess here: ")
        if guess == '0':
            break
        
        guess = guess_list(code, guess)

        if code.check(guess):
            code.display_table()
            print("You win!")
            break
        guesses += 1

def puzzle(total, given, count, settings):
    code = PuzzleGame(total, given, count, settings)

    while True:
        code.display_clues()
        code.list_colors()

        guess = input("Make your guess here: ")
        if guess == '0':
            break

        guess = guess_list(code, guess)

        if code.compare(guess):
            print("You win!")
            break