import random as rand


class DiceRoller:
    def roller(self):
        num = rand.randint(1, 6)
        print("\n",num)


d = DiceRoller()
e_val=input("Dice Roller"
      "\nTo Roll your Dice:"
      "\tPress 'y' to roll 'n' to cancel")
if e_val=='y':
    d.roller()
elif e_val=='n':
    print("Roller Canceled")
else:
    print("Plese select a valid option")

