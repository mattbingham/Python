#!/usr/bin/env python
"""Converts km to miles (and vice versa) from user input"""
__author__ = "Matt Bingham"
__email__ = "mattbingham@outlook.com"

conversion = float(1.60934)

choice = str(input("""
Convert from:
  1. Km to miles.
  2. Miles to km.
"""))

if choice == "1":
	km = float(input("Enter kilometres to convert: "))
	total = km / conversion
	print("{} km is equal to {} miles.".format(km, total))
elif choice == "2":
	miles = float(input("Enter miles to convert: "))
	total = miles * conversion
	print("{} miles is equal to {} km.".format(miles, total))
else:
	print("Invalid entry, try again.")