from codemaker import *

# Player can manually adjust game-specific settings
def options(settings):
    colors = ['Colorless', 'Colored Text', 'Colored Backgrounds']
    color_list = Codemaker.colors_full
    repeat = ['OFF', 'ON']

    # Keep track of whether settings have been changed
    settings_old = settings.copy()

    while True:
        print('1: Peg colors')
        print('2: Mark symbols')
        print('3: Repeat colors')
        print('4: Restore defaults')
        choice = input('Enter a number to select your option or enter 0 to exit. ')
        print()

        # 1: Peg colors
        if choice == "1":
            # Display all pegs with current setting
            print("Current setting: " + colors[settings[0]])
            print("Preview:")
            for color in color_list:
                print(Codemaker.peg_color(Codemaker, color, settings[0]) + ': ' + color)
            print('\nNote that colors may not display properly depending on your system and settings.')
            for i in range(len(colors)):
                print(str(i + 1) + ': ' + colors[i])
            
            # Player can choose between three options
            choice = input('Enter a number to select your option. ')
            if choice.isnumeric() and 0 < int(choice) <= len(colors):
                settings[0] = int(choice) - 1
                print(colors[int(choice) - 1] + " has been selected.\n")
            else:
                print("Invalid choice. Canceling selection.\n")

        # 2: Mark symbols
        elif choice == "2":
            # Display all three symbols that player can change
            print("1. " + settings[1][0] + ' (Correct position)')
            print("2. " + settings[1][1] + ' (Correct color, incorrect positon)')
            print("3. " + settings[1][2] + ' (Incorrect)')

            choice = input('Enter a number to select which symbol to change. ')
            if choice.isnumeric() and 0 < int(choice) <= 3:
                while True:
                    # Player must enter single character to replace symbol with
                    symbol = input("What symbol would you like to replace " + settings[1][int(choice) - 1] + " with? ")
                    if len(symbol) == 1:
                        string_list = list(settings[1])
                        string_list[int(choice) - 1] = symbol
                        settings[1] = "".join(string_list)
                        print(symbol + " has been set.\n")
                        break
                    else:
                        print("Symbol must be exactly one character.\n")
            else:
                print("Invalid choice. Canceling selection.")

        # 3: Repeat colors
        elif choice == "3":
            print("Repeat colors is currently set to " + repeat[int(settings[2])] + ".")
            choice = input("Change to " + repeat[int(not settings[2])] + "? Enter Y to confirm. ")
            if choice.upper() == "Y":
                settings[2] = not settings[2]
                print("Repeat colors is now set to " + repeat[int(settings[2])] + ".\n")
            else:
                print("Repeat colors has not been changed.\n")
        
        # 4: Restore defaults
        elif choice == "4":
            # Allow player to reset options file to original settings
            choice = input("Are you sure you would like to reset to default settings? This change cannot be undone.\nEnter Y to confirm. ")
            if choice.upper() == "Y":
                make_file()
                settings = get_settings()
                settings_old = settings.copy()
                print("Default settings have been restored.\n")
            else:
                print("Canceling selection.\n")

        # Exit options menu and save changes made
        elif choice == "0":
            # Player can choose whether to save changes to file or revert to prior settings
            if settings != settings_old:
                choice = input("Enter Y to save your settings: ")
                if choice == "Y":
                    make_file(settings)
                    print("Changes saved successfully.\n")
                else:
                    settings = settings_old
                    print("Changes canceled.\n")
            return settings
        else:
            print("Invalid choice.\n")

# Create options file
def make_file(settings = [0, "●◌·", True]):
    # Existing file will be overwritten with new settings
    file = open("options.txt", "wt", encoding="utf-8")
    file.write(str(settings[0]) + "\n" + settings[1] + "\n" + str(int(settings[2])))
    file.close()

# Retrieve settings from options file
def get_settings():
    try:
        settings = []
        for line in open("options.txt", "rt", encoding="utf-8"):
            settings.append(line.replace('\n', ''))

        settings[0] = int(settings[0])
        settings[2] = bool(int(settings[2]))

        # Ensure color and mark settings do not cause errors during gameplay
        assert 0 <= settings[0] <= 2
        assert len(settings[1]) == 3
        
        return settings
    
    # Function will fail if file does not exist or is not formatted correctly
    except:
        return False