import random

class Codemaker:

    colors_full = ['B', 'R', 'G', 'Y', 'P', 'C', 'W']

    def __init__(self, total, given):
        self.colors = Codemaker.colors_full[:given]
        self.code = []
        self.table = []
        self.marks = []

        self.guesses = 10

        for i in range(total):
            self.code.append(random.choice(self.colors))

        for i in range(self.guesses):
            self.table.append(["·"] * total)

    def check(self, guess):
        correct = 0
        close = 0
        checked = []

        for i in range(len(self.code)):
            if guess[i] == self.code[i]:
                correct += 1
                checked.append(i)
            elif guess[i] in self.code and i not in checked:
                close += 1
        
        self.update_table(guess)

        missed = len(self.code) - correct - close
        self.marks.append("●" * correct + "◌" * checked + "·" * missed)

        if correct == len(self.code):
            return True
        else:
            return False

    def update_table(self, guess):
        for row in self.table:
            if "·" in row:
                row = guess
                break
    
    def display_table(self):
        for i in range(self.guesses - 1, -1, -1):
            for peg in self.table[i]:
                print(peg, end="  ")
                if "·" not in self.table[i]:
                    print(self.marks[i])
    
    def display_code(self):
        for peg in self.code:
            print(peg, end="  ")

    def list_colors(self):
        print("Available colors: ")
        for color in self.colors:
            print(color, end="  ")