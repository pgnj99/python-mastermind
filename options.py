from codemaker import *

def options(settings):
    colors = ['Colorless', 'Colored Text', 'Colored Backgrounds']
    color_list = Codemaker.colors_full
    repeat = ['OFF', 'ON']
    settings_old = settings.copy()

    while True:
        print('1: Peg colors')
        print('2: Mark symbols')
        print('3: Repeat colors')
        print('4: Restore defaults')
        choice = input('Enter a number to select your option or enter 0 to exit. ')
        print()

        if choice == "1":
            print("Current setting: " + colors[settings[0]])
            print("Preview:")
            for color in color_list:
                print(Codemaker.peg_color(Codemaker, color, settings[0]) + ': ' + color)
            print('\nNote that colors may not display properly depending on your system and settings.')
            for i in range(len(colors)):
                print(str(i + 1) + ': ' + colors[i])
            choice = input('Enter a number to select your option. ')
            if choice.isnumeric and 0 < int(choice) <= len(colors):
                settings[0] = int(choice) - 1
                print(colors[int(choice) - 1] + " has been selected.\n")
            else:
                print("Invalid choice. Canceling selection.\n")

        elif choice == "2":
            print("1. " + settings[1][0] + ' (Correct position)')
            print("2. " + settings[1][1] + ' (Correct color, incorrect positon)')
            print("3. " + settings[1][2] + ' (Incorrect)')
            choice = input('Enter a number to select which symbol to change. ')
            if choice.isnumeric and 0 < int(choice) <= 3:
                while True:
                    symbol = input("What symbol would you like to replace " + settings[1][int(choice) - 1] + " with? ")
                    if len(symbol) == 1:
                        string_list = list(settings[1])
                        string_list[int(choice) - 1] = symbol
                        settings[1] = "".join(string_list)
                        print(symbol + " has been set.\n")
                        break
            else:
                print("Invalid choice. Canceling selection.")

        elif choice == "3":
            print("Repeat colors is currently set to " + repeat[int(settings[2])] + ".")
            choice = input("Change to " + repeat[int(not settings[2])] + "? Enter Y to confirm. ")
            if choice.upper() == "Y":
                settings[2] = not settings[2]
                print("Repeat colors is now set to " + repeat[int(settings[2])] + ".\n")
            else:
                print("Repeat colors has not been changed.\n")

        elif choice == "4":
            choice = input("Are you sure you would like to reset to default settings? This change cannot be undone.\nEnter Y to confirm. ")
            if choice.upper() == "Y":
                make_file()
                settings = get_settings()
                settings_old = settings.copy()
                print("Default settings have been restored.\n")
            else:
                print("Canceling selection.\n")

        elif choice == "0":
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

def make_file(settings = [0, "●◌·", True]):
    file = open("options.txt", "wt", encoding="utf-8")
    file.write(str(settings[0]) + "\n" + settings[1] + "\n" + str(int(settings[2])))
    file.close()

def get_settings():
    try:
        settings = []
        for line in open("options.txt", "rt", encoding="utf-8"):
            settings.append(line.replace('\n', ''))

        settings[0] = int(settings[0])
        settings[2] = bool(int(settings[2]))
        return settings
    except:
        return False