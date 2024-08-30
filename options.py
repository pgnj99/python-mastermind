from codemaker import *

def options(settings):
    colors = ['Colorless', 'Colored Text', 'Colored Backgrounds']
    color_list = Codemaker.colors_full
    repeat = ['ON', 'OFF']
    settings_old = settings

    while True:
        print('1: Peg colors')
        print('2: Mark symbols')
        print('3: Repeat colors')
        print('4: Restore defaults')
        choice = input('Enter a number to select your option or enter 0 to exit. ')

        if choice == "1":
            print("Current setting: " + colors[settings[0]])
            print("Preview:")
            for color in color_list:
                if settings[0] == 0:
                    print(color[0] + ": " + color)
                elif settings[0] == 1:
                    print('\033[' + str(color_list[color]) + 'm' + color[0] + '\033[0m: ' + color)
                elif settings[0] == 2:
                    print('\033[30m\033[' + str(color_list[color] + 10) + 'm' + color[0] + '\033[0m: ' + color)
            print('\nNote that colors may not display properly depending on your system and settings.')
            for i in range(len(colors)):
                print(str(i + 1) + ': ' + colors[i])
            choice = input('Enter a number to select your option. ')
            if choice.isnumeric and 0 < int(choice) <= len(colors):
                settings[0] = int(choice)
                print(colors[int(choice)] + " has been selected.")
            else:
                print("Invalid choice. Canceling selection.")

        elif choice == "2":
            print("1. " + settings[1][0] + '(Correct position)')
            print("2. " + settings[1][1] + '(Correct color, incorrect positon)')
            print("3. " + settings[1][2] + '(Incorrect)')
            choice = input('Enter a number to select which symbol to change. ')
            if choice.isnumeric and 0 < int(choice) <= 3:
                while True:
                    symbol = input("What symbol would you like to replace " + settings[1][int(choice)] + " with? ")
                    if len(symbol) == 1:
                        string_list = list(settings[1])
                        string_list[int(choice)] = symbol
                        settings[1] = "".join(string_list)
                        print(symbol + " has been selected.")
            else:
                print("Invalid choice. Canceling selection.")

        elif choice == "3":
            print("Repeat colors is currently set to " + repeat[int(settings[2])] + ".")
            choice = input("Change to " + repeat[int(not settings[2])] + "? Enter Y to confirm. ")
            if choice.upper() == "Y":
                settings[2] = not settings[2]
                print("Repeat colors is now set to " + repeat[int(settings[2])] + ".")
            else:
                print("Repeat colors has not been changed.")

        elif choice == "4":
            choice = input("Are you sure you would like to reset to default settings? Enter Y to confirm. ")
            if choice.upper() == "Y":
                make_file()
                settings = get_settings()
                print("Default settings have been restored.")
            else:
                print("Canceling selection.")

        elif choice == "0":
            if settings != settings_old:
                choice = input("Enter Y to save your settings: ")
                if choice == "Y":
                    make_file(settings)
                    print("Changes saved successfully.")
                else:
                    settings = settings_old
                    print("Changes canceled.")
            return settings
        else:
            print("Invalid choice.")

def make_file(settings = [0, ["●◌·"], True]):
    file = open("options.txt", "wt")
    file.writelines([str(settings[0]), settings[1], str(int(settings[2]))])
    file.close()

def get_settings():
    try:
        settings = []
        file = open("options.txt", "rt")
        for i in range(3):
            settings.append(file.readlines())
        file.close()

        settings[0] = int(settings[0])
        settings[2] = bool(int(settings[2]))
        return settings
    except:
        return False