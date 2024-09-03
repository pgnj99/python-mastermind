import random

class Codemaker:

    # colors_full dictionary contains all available peg colors with numbers to be used for colored text
    colors_full = {'Blue': 34, 'Red': 31, 'Green': 32, 'Yellow': 93, 'Pink': 95, 'Cyan': 36, 'White': 37}

    def __init__(self, total, given, settings):
        # colors list will only contain colors selected for game
        self.colors = list(self.colors_full.keys())[:given]
        self.marks = []

        # Get variables from settings
        self.color_mode = settings[0]
        self.mark_correct = settings[1][0]
        self.mark_close = settings[1][1]
        self.mark_missed = settings[1][2]
        self.repeat = settings[2]

        self.code = self.make_code(total)

    # Create code for the player to guess
    def make_code(self, total):
        code = []

        # Repeat colors setting will determine whether multiple pegs of the same color can exist in one code
        if self.repeat:
            for i in range(total):
                code.append(random.choice(self.colors))
        else:
            code = random.sample(self.colors, total)
        return code

    # Return code in single-character form
    # Parameter is included for clues or guesses to borrow functionality
    def get_code(self, code = 0):
        if code == 0:
            code = self.code
        return [color[0] for color in code]

    # Create marks for each guess or clue based on code
    def make_marks(self, guess, code):
        correct = 0     # Correct peg, correct position
        close = 0       # Correct peg, incorrect position
        checked = []    # Indexes already checked

        # Convert guess and code to single-character form
        guess = self.get_code(guess)
        code = self.get_code(code)

        # Check each guess character against each code character
        for i in range(len(code)):
            # Increment "correct" when peg is perfect match
            if guess[i] == code[i]:
                correct += 1
                checked.append(i)
            else:
                for j in range(len(code)):
                    # Increment "close" when peg is in incorrect position
                    # Do not increment if peg is already checked or has unchecked perfect match
                    if guess[i] == code[j] and guess[j] != code[j] and j not in checked:
                        close += 1
                        checked.append(j)
                        break
        
        # Remaining pegs will be counted as missed
        missed = len(code) - correct - close
        
        return self.mark_correct * correct + self.mark_close * close + self.mark_missed * missed

    # Print available peg colors
    def list_colors(self):
        print("Available colors: ")
        for color in self.colors:
            print(self.peg_color(color), end="  ")
        print("\n")

    # Apply user-selected color to pegs
    def peg_color(self, text, mode = None):
        # mode parameter allows options to access function before saving settings
        if mode == None:
            mode = self.color_mode

        # Both full color names and single characters can be inserted into text parameter
        if len(text) == 1:
            for color in self.colors_full:
                if text == color[0]:
                    text = color

        # Mode 1: Colorless text
        if mode == 0:
            return text[0]
        # Mode 2: Colored Text
        elif mode == 1:
            return '\033[' + str(self.colors_full[text]) + 'm' + text[0] + '\033[0m'
        # Mode 3: Colored Backgrounds
        elif mode == 2:
            return '\033[30m\033[' + str(self.colors_full[text] + 10) + 'm' + text[0] + '\033[0m'


# Class for classic game mode
class ClassicGame(Codemaker):
    def __init__(self, total, given, settings):
        # Classic game will require table and maximum guesses
        super().__init__(total, given, settings)
        self.table = []
        self.guesses = 10

        # Initialize table with bullet points representing empty pegs
        for i in range(self.guesses):
            self.table.append(["·"] * total)

    # Check whether guess matches code
    def check(self, guess):
        # Start by adding guess to table
        self.update_table(guess)

        # Retrieve guess marks
        mark = self.make_marks(guess, self.code)
        self.marks.append(mark)

        # Player wins if guess equals code
        if guess == self.get_code():
            return True
        else:
            return False

    # Update table with new guess
    def update_table(self, guess):
        for i in range(self.guesses):
            # Guess will be added to first empty row
            if "·" in self.table[i]:
                self.table[i] = guess
                break
    
    # Display full table
    def display_table(self):
        # Iterate backwards in order to show empty guesses at top
        for i in range(self.guesses - 1, -1, -1):
            for peg in self.table[i]:
                if peg == "·":
                    print(peg, end="  ")
                else:
                    print(self.peg_color(peg), end="  ")
            # Marks will not be printed for empty rows
            if "·" not in self.table[i]:
                print(self.marks[i])
            else:
                print()
    
    # Display code at end of game
    def display_code(self):
        for peg in self.code:
            print(self.peg_color(peg), end="  ")
        print("\n")


# Class for puzzle game mode
class PuzzleGame(Codemaker):

    monster_touch = {0: [1, 2, 3], 1: [0, 3, 4], 2: [0, 3, 5], 3: [0, 1, 2, 4, 5, 6], 4: [1, 3, 6], 5: [2, 3, 6], 6: [3, 4, 5]}

    def __init__(self, total, given, count, settings):
        # Puzzle game will require list of clues
        super().__init__(total, given, settings)
        self.clues = []

        # Each clue will be randomly created and treated as guess against code
        # Clues cannot repeat and cannot be the same as code
        while len(self.clues) < count:
            clue = self.make_code(total)
            if clue != self.code and clue not in self.clues:
                self.clues.append(clue)
        
        for clue in self.clues:
            self.marks.append(self.make_marks(clue, self.code))

    # Display list of clues with marks
    def display_clues(self):
        if len(self.code) != 7:
            for i in range(len(self.clues)):
                for peg in self.clues[i]:
                    print(self.peg_color(peg), end="  ")
                print(self.marks[i])
            print()
        else:
            for clue in self.clues:
                print(" " + self.peg_color(clue[0]) + " " + self.peg_color(clue[1]))
                print(self.peg_color(clue[2]) + " " + self.peg_color(clue[3]) + " " + self.peg_color(clue[4]))
                print(" " + self.peg_color(clue[5]) + " " + self.peg_color(clue[6]) + " " + self.marks[self.clues.index(clue)])
                print()


    # Compare guess with clues
    def compare(self, guess):
        # Player wins if guess is consistent with each clue's marks
        for i in range(len(self.clues)):
            # Clue passes if marks between clue and code match marks between guess and clue
            # If marks match for all clues, the player has guessed a winning code
            guessmark = self.make_marks(guess, self.clues[i])
            if guessmark == self.marks[i]:
                print("Clue " + str(i + 1) + " passed!")
            else:
                print("Clue " + str(i + 1) + " failed!")
                print("Please try again.")
                return False
        return True

    
    def make_code(self, total):
        if total != 7:
            return super().make_code(total)

        code = [None] * 7
        available = self.colors.copy()
        used = set()
        order = [[3], [0,4,5], [1,2,6]]

        # Repeat colors setting will determine whether multiple pegs of the same color can exist in one code
        if self.repeat:
            for group in order:
                for num in group:
                    code[num] = random.choice(available)
                    used.add(code[num])
                for color in used:
                    available.remove(color)
                used = set()
        else:
            code = random.sample(self.colors, total)
        return code