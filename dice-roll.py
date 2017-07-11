#!/usr/bin/env python
"""A random number from 1 - 6 is generated with x number of dice"""
__author__ = "Matt Bingham"
__email__ = "mattbingham@outlook.com"

import random
from collections import Counter

#Vars
decorate = "=" * 10
decorate1 = decorate + "="
question = int(input("How many dice do you want to roll? > "))

def dice_list(i):
	lst = []
	count = 1
	total = 0
	c1 = []
	c2 = []
	while i != 0:
		roll = random.randint(1, 6)
		lst.append(roll)
		print("Roll {}: {}".format(count, lst[count-1]))
		if roll < 10:
			print(decorate1)
		else:
			print(decorate)
		i -= 1
		count += 1
	for n in lst:
		total = total + n

	variations = Counter(lst)
	for n in variations:
		c1.append(n)
	print(decorate * 6)
	print("STATS")
	print("Your rolls list   :\t", lst)
	print("Rolls total count :\t", total)
	print("Unique numbers    :\t", c1)
	print("Number consistancy:\t")
	for k,v in variations.items():
	    print(k,"x",v)

#Ask
print(question)
dice_list(question)
