import random

class Codemaker:

    colors_full = {'Blue': 34, 'Red': 31, 'Green': 32, 'Yellow': 93, 'Pink': 95, 'Cyan': 36, 'White': 47}

    def __init__(self, total, given, settings):
        self.colors = dict(list(self.colors_full.items())[:given])
        self.code = self.make_code(total)
        self.marks = []

        self.settings = settings
        self.mark_correct = self.settings[1][0]
        self.mark_close = self.settings[1][1]
        self.mark_missed = self.settings[1][2]

    def make_code(self, total):
        code = []
        for i in range(total):
            code.append(random.choice(list(self.colors.keys())))
        return code

    def get_code(self, code = 0):
        if code == 0:
            code = self.code
        return [color[0] for color in code]

    def make_marks(self, guess, code):
        correct = 0
        close = 0
        checked = []
        guess = self.get_code(guess)
        code = self.get_code(code)

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
            print(self.peg_color(color), end="  ")
        print()

    def peg_color(self, text, settings = 0):
        if settings == 0:
            settings = self.settings
        
        text = text[0]

        if settings[0] == 0:
            return text
        elif settings[0] == 1:
            return '\033[' + str(self.colors_full[text]) + 'm' + text + '\033[0m'
        elif settings[0] == 2:
            return '\033[30m\033[' + str(self.colors_full[text] + 10) + 'm' + text + '\033[0m'



class ClassicGame(Codemaker):
    def __init__(self, total, given, settings):
        super().__init__(total, given, settings)
        self.table = []
        self.guesses = 10

        for i in range(self.guesses):
            self.table.append(["·"] * total)

    def check(self, guess):
        self.update_table(guess)

        mark = self.make_marks(guess, self.code)
        self.marks.append(mark)

        if guess == self.get_code():
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
                print(self.peg_color(peg), end="  ")
            if "·" not in self.table[i]:
                print(self.marks[i])
            else:
                print()
    
    def display_code(self):
        for peg in self.code:
            print(self.peg_color(peg), end="  ")
        print()


class PuzzleGame(Codemaker):
    def __init__(self, total, given, count, settings):
        super().__init__(total, given, settings)
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
                print(self.peg_color(peg), end="  ")
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