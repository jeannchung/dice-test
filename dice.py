import random

def roll(sides=6):
    roll_number = random.randint(1, sides)
    return roll_number

def main():
    sides = 6
    rolling = True
    while rolling:
        roll_again = input("Ready to roll? Press ENTER to roll. Press Q to quit.")
        if roll_again.lower() != 'q':
            roll_number = roll(sides)
            print("You rolled a " + str(roll_number))
        else:
            print("Thanks for playing.")

main()
