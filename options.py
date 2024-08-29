from codemaker import *

def options(settings):
    colors = ['Colorless', 'Colored Text', 'Colored Backgrounds']
    repeat = ['ON', 'OFF']

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
            break
        else:
            print("Invalid choice.")