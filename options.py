from codemaker import *

def options(settings):
    colors = ['Colorless', 'Colored Text', 'Colored Backgrounds']
    repeat = ['ON', 'OFF']
    settings_old = settings

    while True:
        print('1: Peg colors')
        print('2: Mark symbols')
        print('3: Repeat colors')
        choice = input('Enter a number to select your option or enter 0 to exit. ')
        if choice == "1":
            print("Current setting: " + colors[settings[0]])
            print("Preview:")
            pass
        elif choice == "2":
            pass
        elif choice == "3":
            print("Repeat colors is currently set to " + repeat[int(settings[2])] + ".")
            choice = input("Change to " + repeat[int(not settings[2])] + "? (Y/N) ")
            if choice.upper() == "Y":
                settings[2] = not settings[2]
                print("Repeat colors is now set to " + repeat[int(settings[2])] + ".")
            elif choice.upper() == "N":
                print("Repeat colors has not been changed.")
            else:
                print("Invalid choice.")
        elif choice == "0":
            if settings != settings_old:
                choice = input("Enter Y to save your settings: ")
                if choice == "Y":
                    make_file(settings)
                    print("Changes saved successfully.")
                else:
                    settings = settings_old
                    print("Changes canceled.")
            break
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