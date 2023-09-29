import random as rand


class DiceRoller:
    dice = {1: '\u2680', 2: '\u2681', 3: '\u2682', 4: '\u2683', 5: '\u2684', 6: '\u2685'}

    def roller(self):
        num = rand.randint(1, 6)
        for i in self.dice:
            if i == num:
                print("\n\t",self.dice[i])


d = DiceRoller()  # Instance created for the class

e_val=True

# Checking the input and providing appropriate response
while e_val:
    e_val = input("\nDice Roller"
                  "\nTo Roll your Dice:"
                  "\tPress 'r' to roll 'c' to cancel")  # Taking input from the user
    if e_val == 'r':
        d.roller()
    elif e_val == 'c':
        print("Roller Canceled")
        break
    else:
        print("Plese select a valid option")
        continue



