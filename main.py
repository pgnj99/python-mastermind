print('MASTERMIND')
print('1: Classic')
print('2: Puzzle')
print('3: Options')

# This loop will run for as long as the player wants to continue playing
while True:
    choice = input('Enter a number to select your mode or enter 0 to exit. ')
    if choice == "1":
        play(1)
    elif choice == "2":
        play(2)
    elif choice == "3":
        play(3)
    elif choice == "0":
        print("Thank you for playing!")
        break
    else:
        print("Invalid choice.")