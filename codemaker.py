import random

class Codemaker:

    colors_full = ['B', 'R', 'G', 'Y', 'P', 'C', 'W']

    def __init__(self, total, given):
        self.colors = Codemaker.colors_full[:given]
        self.code = []
        for i in range(total):
            self.code.append(random.choice(self.colors))

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
        
        missed = len(self.code) - correct - close
        print("●" * correct + "◌" * checked + "·" * missed)


    def list_colors(self):
        print("Available colors:")
        for color in self.colors:
            print(color, end="  ")