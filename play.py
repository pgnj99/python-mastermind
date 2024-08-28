from codemaker import *

def classic(total, given):
    code = Codemaker(total, given)
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

    code.check(guess)