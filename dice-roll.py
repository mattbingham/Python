#!/usr/bin/env python
"""A random number from 1 - 6 is generated with x number of dice"""
__author__ = "Matt Bingham"
__email__ = "mattbingham@outlook.com"

import random 

#Vars
decorate = "=" * 20
question = int(input("How many dice do you want to roll? > "))

def dice_list(i):
	lst = []
	count = 1
	while i != 0:
		roll = random.randint(1, 6)
		lst.append(roll)
		print("Roll {}: {}".format(count, lst[count-1]))
		print(decorate)
		i -= 1
		count += 1
	print("Your total rolls are", lst)

#Ask
print(question)
dice_list(question)
