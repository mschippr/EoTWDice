#!/usr/bin/env python
from random import randint
from collections import OrderedDict

class Die(object):
    """
    Creates a die class for use with a dice rolling utility

    """
    d_sides = None
    def __init__(self, sides = 6):
        self._sides = sides
        self._value = None
        self.roll()

    def roll(self):
        """
        Generate a random integer based off the number of sides
        """
        self._value = randint(1, self._sides)
        return self._value

    def __str__(self):
        """
        Return string containing dice sides and result
        """
        return "Die with {} sides.  Result : {}".format(self._sides, self._value)

def banner():
    """
    Print out in console upon running script
    """
    print("-" * 10)
    print("The End of the World Dice Roller")
    print("-" * 10)

def dice_cup(p, n):

    dice_roll = {}
    dice_roll[0] = [Die(6).roll() for _ in range(int(p))]
    dice_roll[1] = [Die(6).roll() for _ in range(int(n))]

    return dice_roll

def calculate_results(roll, stat):
    sortedrolls = OrderedDict.fromkeys(roll)

    return sortedrolls

def print_dice(d):
    """
    Converts list of dice results into string and prints results and total
    """
    print(d)
    pdice_str = ','.join(map(str, d[0]))
    print("You rolled: {}\nTotal Pos: {}".format(pdice_str))
    ndice_str = ','.join(map(str, d[1]))
    print("You rolled: {}\nTotal Neg: {}".format(ndice_str))

def engine():
    banner()
    # Asks for a number of dice and verifies that it's a number

    # Asks for a number of dice and verifies that it's a number
    while True:
        try:
            stat = int(input("Input Attribute Score?\n>"))
            break
        except(TypeError, ValueError):
            print("Please enter a number\n")

    while True:
        try:
            p = int(input("How many positive dice?\n>"))
            break
        except(TypeError, ValueError):
            print("Please enter a number\n")

    # Asks for a number of dice and verifies that it's a number
    while True:
        try:
            n = int(input("How many negative dice?\n>"))
            break
        except(TypeError, ValueError):
            print("Please enter a number\n")

    roll = dice_cup(p, n)
    results = calculate_results(roll, stat)
    print_dice(roll)

def main():
    engine()

if __name__ == "__main__":
    main()