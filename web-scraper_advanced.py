#!/usr/bin/env python
"""Get headings or links from the user input URL"""
__author__ = "Matt Bingham"
__email__ = "mattbingham@outlook.com"


"""In order to use this script, you'll need to:
pip install beautifulsoup4
pip install lxml
pip install requests
"""

import requests
from bs4 import BeautifulSoup

# Create a variable with the url
url = str(input("Enter the URL you want to parse headings or links from: "))
# Prettify stuff
decoration = "=" * 20
# Use requests to get the contents
r = requests.get(url)
# Get the text of the contents
html_content = r.text
# Convert the html content into a beautiful soup object
soup = BeautifulSoup(html_content, 'lxml')

print(decoration)
question = """
Find links headings or paragraphs?
Press 1 for links
Press 2 for headings
Press 3 for paragraphs
> """
user = int(input(question))
title = "{}\nPage title: \n\t{}".format(decoration, soup.title.string)

# Make sure user is entering a correct number
while user not in range(1, 4):
	print("That input is not valid, please enter a number 1 - 4 > ")
	user = int(input(question))

"""Section defines what is input into the Selection class"""
def q(user):
	if user == 1:
		a.links(user)
	elif user == 2:
		a.headings(user)
	else:
		user == 3
		a.paragraphs(user)

"""Takes the user input and selection and outputs below"""
class Selection(object):

	def links(self, user):
		d = "links"
		a = soup.find_all('a')
		print(title)
		print("{}\n{} for {}".format(decoration, d, url))
		for i in a:
			print("\t", i.get('href'))

	def headings(self, user):
		d = "headings"
		h = input("{}Enter the heading type you want.\nPress 1 for h1 {}\nPress 2 for h2 {} and so on. > ".format(decoration, d, d))
		user = "h{}".format(h)
		h = soup.find_all(user)
		print(title)
		print(decoration, "\n{} {}:".format(user, d))
		# If no headings found
		if not h:
			print("\tNo {} {} found".format(user, d))
		else:
			for i in h:
				print("\t", i.get_text())
		
	def paragraphs(self, user):
		d = "paragraphs"
		# Save paragraphs in list
		print(title)
		print(decoration)
		for n in soup.find_all('p'):
			print(n.text)

#Run the program
print(user)
a = Selection()
q(user)
