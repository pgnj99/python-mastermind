from codemaker import *

def classic(total, given):
    code = Codemaker(total, given)
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
        guesslist = []

        while True:
            for peg in guess:
                if peg.isalpha():
                    guesslist.append(peg.upper())
            
            if len(guesslist) != len(code.code):
                guess = input("Invalid guess. Try again: ")
            else:
                break

        if code.check(guesslist):
            code.display_table()
            print("You win!")
            break
        guesses += 1