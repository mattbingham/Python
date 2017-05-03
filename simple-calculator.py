#!/usr/bin/env python
"""Simple user input and calculation"""
__author__ = "Matt Bingham"
__email__ = "mattbingham@outlook.com"

no1 = float(input("Enter a number > "))
fn1 = str(input("""Enter a function: 
Press 1 or +
Press 2 or -
Press 3 or *
Press 4 or /\n> """))
no2 = float(input("Enter a number > "))

if (fn1 == "1") or (fn1 == "+"):
	tot = no1 + no2
elif (fn1 == "2") or (fn1 == "-"):
	tot = no1 - no2
elif (fn1 == "3") or (fn1 == "*"):
	tot = no1 * no2
elif (fn1 == "4") or (fn1 == "/"):
	tot = no1 / no2
else:
	tot = "You did not enter a valid function."

print(tot)