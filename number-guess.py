#!/usr/bin/env python
"""Guess a number, returns higher or lower if incorrect"""
__author__ = "Matt Bingham"
__email__ = "mattbingham@outlook.com"

"""
TO-DO
Assign to definitions
Compensate for user input error
"""
import random

number = random.randint(1, 10)
go = 1
gos = 3
decorate = "=" * 20
print(decorate)
print("Can you guess the number between 1 and 10?")
print("Guess", go, "of", gos)
guess = int(input("> "))

while guess != number:
	print(decorate)
	print("Nope, that's not correct.")
	print("Guess", go, "of", gos)
	if gos == go:
		print("To many wrong answers - better luck next time!")
		break
	else:
		if guess > number:
			print("You need to go lower.")
			guess = int(input("> "))
			go += 1
		else:
			print("You need to go higher.")
			guess = int(input("> "))
			go += 1
if guess == number:
	print(decorate)
	print("Good guess! You win!")