# msdie.py
"""Class definition for an n-sided die."""

from random import randrange


class MSDie:
    """A class to represent a multi-sided die."""

    def __init__(self, n):
        """Creates a multi-sided die with the given number of sides
        as a parameter."""
        self.sides = n
        self.value = 1

    def roll(self):
        """Rolls the dice to a random face."""
        self.value = randrange(1, self.sides + 1)

    def getValue(self):
        """Shows the value of the current face."""
        return self.value

    def setValue(self, val):
        """Sets the value of the die's face to the given parameter."""
        self.value = val


def main():
    die1 = MSDie(6)
    die1.setValue(4)
    die1.getValue()
    print(die1.getValue())


main()
