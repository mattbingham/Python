#!/usr/bin/env python
"""A random numbe from 1 - 6 is generated"""
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
user = print("You rolled a {}".format(dice))