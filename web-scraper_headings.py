#!/usr/bin/env python
"""Get headings from the user input URL"""
__author__ = "Matt Bingham"
__email__ = "mattbingham@outlook.com"


"""In order to use this script, you'll need to:
pip install beautifulsoup4
"""

import requests
from bs4 import BeautifulSoup

# Create a variable with the url
url = str(input("Enter the URL you want to parse headings from: "))
decoration = "=" * 20

# Use requests to get the contents
r = requests.get(url)
# Get the text of the contents
html_content = r.text
# Convert the html content into a beautiful soup object
soup = BeautifulSoup(html_content, 'lxml')
# View the title tag of the soup object
soup.title
# View the string within the title tag
soup.title.string

# Save headings to variables
h1 = soup.find_all('h1')
h2 = soup.find_all('h2')
h3 = soup.find_all('h3')
h4 = soup.find_all('h4')
h5 = soup.find_all('h5')
print(decoration)
print("Heading for page:\n{}".format(soup.title.string))

h = str(input("""
	Which title would you like to print? :
	Press 1 for all h1 headings
	Press 2 for all h2 headings
	Press 3 for all h3 headings
	Press 4 for all h4 headings
	Press 5 for all h5 headings
	Press 6 for all headings > \n
	"""))

h = "h{}".format(h)
print(h)

def headings(h):
	# Get heading number input



	# Loop and print out all input headers


"""
if get_titles == "1":
	print("H1 headers:\n-----------")
	for h in h1:
		print(h.get_text())

elif get_titles == "2":
	print("H2 headers:\n-----------")
	for h in h2:
		print(h.get_text())

elif get_titles == "3":
	print("H3 headers:\n-----------")
	for h in h3:
		print(h.get_text())

elif get_titles == "4":
	print("H4 headers:\n-----------")
	for h in h4:
		print(h.get_text())

elif get_titles == "5":
	print("H5 headers:\n-----------")
	for h in h5:
		print(h.get_text())

elif get_titles == "6":
	print(decoration)
	print("H1 headers:\n-----------")
	for h in h1:
		print(h.get_text())
		print(decoration)

	print("H2 headers:\n-----------")
	for h in h2:
		print(h.get_text())
	print(decoration)

	print("H3 headers:\n-----------")
	for h in h3:
		print(h.get_text())
	print(decoration)

	print("H4 headers:\n-----------")
	for h in h4:
		print(h.get_text())
	print(decoration)

	print("H5 headers:\n-----------")
	for h in h5:
		print(h.get_text())
	# Get all headings
	else:
		tot = "You did not enter a valid function."

"""