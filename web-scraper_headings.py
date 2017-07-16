#!/usr/bin/env python
"""Get headings from the user input URL"""
__author__ = "Matt Bingham"
__email__ = "mattbingham@outlook.com"


"""In order to use this script, you'll need to:
pip install beautifulsoup4
pip install lxml
pip install requests

Work needed: Validation for incorrect input and no header return text
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

print(decoration)
print("Page Heading:\n{}".format(soup.title.string))

user = input("""
	Which title would you like to print? :
	Press 1 for all h1 headings
	Press 2 for all h2 headings
	Press 3 for all h3 headings
	Press 4 for all h4 headings
	Press 5 for all h5 headings
	""")

# Save BS heading string for heading number
user = "h{}".format(user)

# Save heading number to BS search
h = soup.find_all(user)

print(decoration)
print("{} headers:\n-----------".format(user))
for i in h:
	print(i.get_text())
	

print("""
Find links headings or paragraphs?
Press 1 for links
Press 2 for headings
Press 3 for paragraphs
""")
a = soup.find_all('a')[0:5]