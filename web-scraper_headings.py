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
url = input("Enter the URL you want to parse headings from: ")
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
