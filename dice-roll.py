#!/usr/bin/env python
"""A random number from 1 - 6 is generated"""
__author__ = "Matt Bingham"
__email__ = "mattbingham@outlook.com"

import random 

dice = random.randint(1,6)
choice = "y"
decorate = "=" * 20

# First roll
output = print("You rolled a {}".format(dice))

# Ask user if they want to roll again
while choice == "y":
	choice = input("Roll again? Y or N > ").lower()
	print(decorate)
	if choice not in ("y", "n"):
		print("Sorry I didn't understand that.")
	elif choice == "y":
		dice = random.randint(1,6)
		output = print("You rolled a {}".format(dice))
	else:
		print("Au revoir!")