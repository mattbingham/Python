#!/usr/bin/env python
"""Adds a dog and dogs owner information"""
__author__ = "Matt Bingham"
__email__ = "mattbingham@outlook.com"
__copyright__ = "Borrowed and ammended from the Self Taught Programmer by Cory Althoff"

class Dog():
	"""Adds a dog and collar tag"""
	def __init__(self, name, breed, owner):
		self.name = name
		self.breed = breed
		self.owner = owner

class Owner():
	"""Adds an owner"""
	def __init__(self, name):
		self.name = name

own_name	= input("What's your name? > ")
dog_name 	= input("What's your dog's name? > ")
dog_breed	= input("What's your dog's breed? > ")
owns 		= Owner(own_name)
dogs		= Dog(own_name, dog_breed, owns)

print("The owner of", dog_name, "the", dogs.breed, "is", dogs.owner.name)
