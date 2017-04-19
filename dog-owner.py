"""
Author: M. Bingham
Description: Allows users to input dogs and owners
"""

class Dog():
	"""Adds a dog and collar tag"""
	def __init__(self, name, tag, owner):
		self.name = name
		self.tag = tag
		self.owner = owner

class Owner():
	"""Adds an owner"""
	def __init__(self, name):
		self.name = name

owner1 = input("Enter your name > ")
dog1name = input("Enter your dogs name > ")
dog1tag = input("Enter your dogs tag > ")

print("""
	  Dog: {} | ID: {} 
	  Owner: {}
	  """.format(dog1name, dog1tag, owner1))
