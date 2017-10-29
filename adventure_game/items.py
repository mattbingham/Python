#!/usr/bin/env python3
"""Part of 'adventure_game'. Items file."""
__author__ = "Matt Bingham"
__email__ = "mattbingham@outlook.com"


class Item():
	"""The base class for all items"""
	def __init__(self, name, description):
		super(Item, self).__init__()
		self.name = name
		self.description = description

		def __str__(self):
			return "{}\n=====\n{}".format(self.name, self.description)
