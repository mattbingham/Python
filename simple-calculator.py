__author__ = "Matt Bingham"
__email__ = "mattbingham@outlook.com"

no1 = float(input("Enter a number > "))
fn1 = str(input("""Enter a function: 
Press 1 for +
Press 2 for -
Press 3 for *
Press 4 for /\n> """))
no2 = float(input("Enter a number > "))

if fn1 == "1":
	tot = no1 + no2
elif fn1 == "2":
	tot = no1 - no2
elif fn1 == "3":
	tot = no1 * no2
elif fn1 == "4":
	tot = no1 / no2
else:
	tot = "You did not enter a valid function."

print(tot)