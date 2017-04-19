#!/usr/bin/env python
"""A random number from 1 - 6 is generated"""
__author__ = "Matt Bingham"
__email__ = "mattbingham@outlook.com"

"""
TODO
- User input
-- How many dice need rolling?
-- Generate if loop for each dice of input given 
"""

import random 
dice = random.randint(1,6)
output = print("You rolled a {}".format(dice))

user = input("Roll again? Y or N > ").lower()
if user == "y":
	number_rolls = 1
	user = input("Roll again? Y or N > ").lower()
	while number_rolls != 0:
		output = print("You rolled a {}".format(dice))
		user = input("Roll again? Y or N > ").lower()
		if user != "y":
			print("Bye bye!")
		number_rolls -= 1
	
