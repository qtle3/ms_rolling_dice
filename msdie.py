# msdie.py
# Class definition for an n-sided die.

from random import randrange


class MSDie:
    # A class to represent a multi-sided die.

    def __init__(self, n):
        # Creates a multi-sided die with the given number of sides as a parameter.
        self.sides = n
        self.value = 1

    def roll(self):
        # Rolls the dice to a random face.
        self.value = randrange(1, self.sides + 1)

    def getValue(self):
        # Shows the value of the current face.
        return self.value

    def setValue(self, val):
        # Sets the value of the die's face to the given parameter.
        self.value = val


# The main function is used to test the MSDie class.
def main():
    die1 = MSDie(6)
    die1.setValue(1)
    die1.roll()
    die1.getValue()
    print("The roll of dice #1 is ", die1.getValue())


def die2():
    die2 = MSDie(8)
    die2.setValue(3)
    die2.roll()
    die2.getValue()
    print("The roll of dice #2 is", die2.getValue())


main()
die2()
