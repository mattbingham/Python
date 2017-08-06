#!/usr/bin/env python
"""A random number from 1 - 6 is generated with x number of dice"""
__author__ = "Matt Bingham"
__email__ = "mattbingham@outlook.com"

import random
from collections import Counter

question = int(input("How many dice do you want to roll? > "))

def line(length):
	decorate = "=" * length
	print(decorate)

class Dice():
	def __init__(self, i):
		lst = []
		count = 1
		total = 0
		c1 = []
		c2 = []
		while i != 0:
			roll = random.randint(1, 6)
			lst.append(roll)
			print("Roll {}: {}".format(count, lst[count-1]))
			i -= 1
			count += 1
		for n in lst:
			total = total + n
		variations = Counter(lst)
		for n in variations:
			c1.append(n)
		Dice.output(lst, total, c1, variations)

	def output(lst, total, c1, variations):
		line(10)
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

#Ask
print(question)
line(10)
Dice(question)