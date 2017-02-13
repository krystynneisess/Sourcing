"""
Automating shopping cart for Digikey orders.
"""
import csv
import time
import os
import readline
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException 
from selenium.common.exceptions import NoAlertPresentException

class DigikeyAutomator:
	
	""" Initializes dictionary that maps each URL to its quantity.
	"""
	def __init__(self):
		self.listURLs = {}
		self.driver = None
		self.qtyField = None
		self.x = 0
	

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

		try:
			self.driver.find_element_by_name("ctl00$ctl00$mainContentPlaceHolder$mainContentPlaceHolder$btnAddToOrder").click()
		except NoSuchElementException:
			x = 0

"""Processes a Digikey CSV file containing quantity and URL.
"""
def main(fileName):
	automator = DigikeyAutomator()
	# Populate dictionary of URLs
	automator.get_URLs(fileName)
	automator.driver = webdriver.Chrome("C:/Users/Kimberly/Desktop/chromedriver.exe")
	# Hard-coded URL that enables us to disable the pop-up for adding future products to cart
	""" This product, with part number 311-130GRCT-ND, will show up in the shopping cart 
		in one of the following ways:
		(1) Product is one of the products to be ordered but the quantity is wrong.
		(2) Product is not one of the products to be ordered.
		In both cases, take appropriate action in deleting or changing the quantity. 
	"""
	# Hard-coded in trying to navigate through the problem of the pop-up
	automator.listURLs["http://www.digikey.com/product-detail/en/yageo/RC0603JR-07130RL/311-130GRCT-ND"] = 1
	automator.fill_form("http://www.digikey.com/product-detail/en/yageo/RC0603JR-07130RL/311-130GRCT-ND");
	automator.submit_form("http://www.digikey.com/product-detail/en/yageo/RC0603JR-07130RL/311-130GRCT-ND");
	time.sleep(10)

	# Fill form for each URL
	for url in automator.listURLs.keys():
		automator.fill_form(url)
		automator.submit_form(url)
	automator.driver.get(automator.driver.current_url)
	webID = automator.driver.find_element_by_id("ctl00_ctl00_topContentPlaceHolder_lblWebID").text
	accessID = automator.driver.find_element_by_id("ctl00_ctl00_topContentPlaceHolder_lblAccessID").text

	# Write shopping cart info to text file
	with open('digikey_shoppingCart.txt', 'w') as f:
		f.write("DigiKey Shopping Cart\n")
		f.write("Web ID: " + str(webID) + "\n")
		f.write("Access ID: " + str(accessID))

"""Call the Main function."""
if __name__ == '__main__':
	s = input("Please input your DigiKey file: ")
	main(s)