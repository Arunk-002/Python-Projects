import random as rand


class DiceRoller:
    def roller(self):
        num = rand.randint(1, 6)  # Random number is genrated and assigned to num variable
        print("\n", num)


d = DiceRoller()  # Instance created for the class

e_val = input("Dice Roller"
              "\nTo Roll your Dice:"
              "\tPress 'y' to roll 'n' to cancel")  # Taking input from the user
# Checking the input and providing appropriate response 
if e_val == 'y':
    d.roller()
elif e_val == 'n':
    print("Roller Canceled")
else:
    print("Plese select a valid option")
