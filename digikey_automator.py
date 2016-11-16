"""
Automating shopping cart for Digikey orders.
"""
import csv
import time
import os
import readline
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class DigikeyAutomator:
	
	""" Initializes dictionary that maps each URL to its quantity.
	"""
	def __init__(self):
		self.listURLs = {}
		self.driver = None
		self.qtyField = None

	""" Reads in CSV_FILE and puts URLs into listURLs. COULD POSSIBLY DO IN MAIN
	"""
	def get_URLs(self, csv_file):
		with open(csv_file, 'rt', encoding = 'ISO-8859-1') as f:
			reader = csv.reader(f)
			next(reader) # Don't need to keep first row
			# Iterate through rows of the reader
			for row in reader:
				self.listURLs[row[1]] = int(row[0])

	"""Fill out form for one URL.
	"""
	def fill_form(self, url):
		self.driver.get(url)
		# Get quantity text field
		self.qtyField = self.driver.find_element_by_name("qty")
		# Populate quantity in text field
		self.qtyField.send_keys(self.listURLs[url])

	"""Submit shopping cart form.
	"""
	def submit_form(self, url):
		self.driver.find_element_by_id("addtoorderbutton").click()
		self.driver.refresh()

"""Processes a Digikey CSV file containing quantity and URL.
"""
def main(fileName):
	automator = DigikeyAutomator()
	# Populate dictionary of URLs
	automator.get_URLs(fileName)
	automator.driver = webdriver.Chrome("C:/Users/Kimberly/Desktop/chromedriver.exe")
	# Fill form for each URL
	for url in automator.listURLs.keys():
		automator.fill_form(url)
		automator.submit_form(url)
	automator.driver.get(automator.driver.current_url)
	webID = automator.driver.find_element_by_id("ctl00_ctl00_topContentPlaceHolder_lblWebID").text
	accessID = automator.driver.find_element_by_id("ctl00_ctl00_topContentPlaceHolder_lblAccessID").text

	with open('digikey_shoppingCart.txt', 'w') as f:
		f.write("DigiKey Shopping Cart\n")
		f.write("Web ID: " + str(webID) + "\n")
		f.write("Access ID: " + str(accessID))

"""Call the Main function."""
if __name__ == '__main__':
	#s = input("Please input your DigiKey file: ")
	main("DigiKey_url.csv")