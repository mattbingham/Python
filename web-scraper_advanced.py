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

user = int(input("""
Find links headings or paragraphs?
Press 1 for links
Press 2 for headings
Press 3 for paragraphs
> """))

"""Section defines what is input input the Selection class"""
def q(user):
	if user == 1:
		a.links(user)
	elif user == 2:
		a.headings(user)
	elif user == 3:
		a.paragraphs(user)
	else:
		print("That input is not valid.")

class Selection(object):
	"""Takes the user input and selection and outputs below"""

	def links(self, user):
		d = "links"
		a = soup.find_all('a')
		for i in a:
			print("\t", i.get_text)
		print(a)		

	def headings(self, user):
		d = "headings"
		h = input("{}\nPress 1 for h1 {}\nPress 2 for h2 {}\nPress 3 for h3 {}\nPress 4 for h4 {} > ".format(decoration, d, d, d, d))
		print("{}\nPage title: \n\t{}".format(decoration, soup.title.string))
		user = "h{}".format(h)
		h = soup.find_all(user)
		print(decoration, "\n{} {}:".format(user, d))
		for i in h:
			print("\t", i.get_text())
		
	def paragraphs(self, user):
		d = "paragraphs"
		n = int(input("How many paragraphs do you want to output? > "))
		p = soup.find_all('p')[0:n]
		print(decoration, p)

#Run the program
print(user)
a = Selection()
q(user)