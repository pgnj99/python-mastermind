import random

class Codemaker:

    colors_full = ['B', 'R', 'G', 'Y', 'P', 'C', 'W']
    mark_correct = "●"
    mark_close = "◌"
    mark_missed = "·"

    def __init__(self, total, given):
        self.colors = Codemaker.colors_full[:given]
        self.code = self.make_code(total)
        self.marks = []

    def make_code(self, total):
        code = []
        for i in range(total):
            code.append(random.choice(self.colors))
        return code

    def make_marks(self, guess, code):
        correct = 0
        close = 0
        checked = []

        for i in range(len(code)):
            if guess[i] == code[i]:
                correct += 1
                checked.append(i)
            else:
                for j in range(len(code)):
                    if guess[i] == code[j] and guess[j] != code[j] and j not in checked:
                        close += 1
                        checked.append(j)
                        break
        
        missed = len(code) - correct - close
        
        return self.mark_correct * correct + self.mark_close * close + self.mark_missed * missed

    def list_colors(self):
        print("Available colors: ")
        for color in self.colors:
            print(color, end="  ")
        print()


class ClassicGame(Codemaker):
    def __init__(self, total, given):
        super().__init__(total, given)
        self.table = []
        self.guesses = 10

        for i in range(self.guesses):
            self.table.append(["·"] * total)

    def check(self, guess):
        self.update_table(guess)

        mark = self.make_marks(guess, self.code)
        self.marks.append(mark)

        if guess == self.code:
            return True
        else:
            return False

    def update_table(self, guess):
        for i in range(self.guesses):
            if "·" in self.table[i]:
                self.table[i] = guess
                break
    
    def display_table(self):
        for i in range(self.guesses - 1, -1, -1):
            for peg in self.table[i]:
                print(peg, end="  ")
            if "·" not in self.table[i]:
                print(self.marks[i])
            else:
                print()
    
    def display_code(self):
        for peg in self.code:
            print(peg, end="  ")
        print()


class PuzzleGame(Codemaker):
    def __init__(self, total, given, count):
        super().__init__(total, given)
        self.clues = []

        while len(self.clues) < count:
            clue = self.make_code(total)
            if clue != self.code and clue not in self.clues:
                self.clues.append(clue)
        
        for clue in self.clues:
            self.marks.append(self.make_marks(clue, self.code))

    def display_clues(self):
        for i in range(len(self.clues)):
            for peg in self.clues[i]:
                print(peg, end="  ")
            print(self.marks[i])

    def compare(self, guess):
        for i in range(len(self.clues)):
            guessmark = self.make_marks(guess, self.clues[i])
            if guessmark == self.marks[i]:
                print("Clue " + str(i + 1) + " passed!")
            else:
                print("Clue " + str(i + 1) + " failed!")
                print("Please try again.")
                return False
        return True