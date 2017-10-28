#!/usr/bin/env python3
"""A random number from 1 - 6 is generated with x number of dice"""
__author__ = "Matt Bingham"
__email__ = "mattbingham@outlook.com"

import random
from collections import Counter


def question():
	dice_rolls = int(input("How many dice do you want to roll? > "))
	Dice(dice_rolls)
	print("=" * 10)

class Dice():
	def __init__(self, dice_rolls):
		lst, c1, c2, count, total = [], [], [], 1, 0
		while dice_rolls != 0:
			roll = random.randint(1, 6)
			lst.append(roll)
			print("Roll {}: {}".format(count, lst[count-1]))
			dice_rolls -= 1
			count += 1
		for n in lst:
			total = total + n
		variations = Counter(lst)
		for n in variations:
			c1.append(n)
		Dice.output(lst, total, c1, variations)

	def output(lst, total, c1, variations):
		print("=" * 10)
		print("STATS")
		print("Your rolls list   :\t", lst)
		print("Rolls total count :\t", total)
		print("Unique numbers    :\t", c1)
		print("Number consistancy:\t")
		for k,v in variations.items():
			if v == 1:
				print(k, "rolled 1 time.")
			else:
			    print(k,"rolled", v, "times.")

if __name__ == "__main__":
	question()