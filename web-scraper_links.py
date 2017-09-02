#!/usr/bin/env python
"""Get links from the user input URL"""
__author__ = "Matt Bingham"
__email__ = "mattbingham@outlook.com"


"""In order to use this script, you'll need to:
pip install beautifulsoup4
pip install lxml
pip install requests
"""

import requests
from bs4 import BeautifulSoup

decoration = "=" * 20

def get_stuff():
	url = str(input("Enter the URL you want to parse links from: "))
	r = requests.get(url)
	html_content = r.text
	soup = BeautifulSoup(html_content, 'lxml')
	# show_stuff
	show_stuff(soup, url)

def show_stuff(soup, url):
	print(decoration)
	title = "{}\nPage title: \n\t{}".format(decoration, soup.title.string)
	a = soup.find_all('a')
	print(title)
	print("{}\nLinks for {}".format(decoration, url))
	for i in a:
		print("\t", i.get('href'))

#Run the program
if __name__ == '__main__':
    get_stuff()
