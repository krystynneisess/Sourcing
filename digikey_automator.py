"""
Automating shopping cart for Digikey orders.
"""
import csv
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
		self.driver = webdriver.Chrome("C:/Users/Kimberly/Desktop/chromedriver.exe")
		self.driver.get(url)
		# Get quantity text field
		qtyField = self.driver.find_element_by_name("qty")
		# Populate quantity in text field
		qtyField.send_keys(self.listURLs[url])

	"""Submit shopping cart form.
	"""
	def submit_form(self, url):
		# get SUBMIT button
		#submitButton = driver.find_element_by_id("addtoorderbutton")
		# click SUBMIT
		#submitButton.click()

		# OR
		form = self.driver.find_element_by_id("update-quantity")
		form.submit()

		# Clear the contents of the QUANTITY text field
		qtyField.clear()

		# Close the driver
		self.driver.close()

"""Processes a Digikey CSV file containg quantity and URL.
"""
def main(fileName):
	automator = DigikeyAutomator()
	# Populate dictionary of URLs
	automator.get_URLs(fileName)
	# Fill form for each URL
	self.driver = webdriver.Chrome()
	for url in automator.listURLs.keys():
		automator.fill_form(url)
		automator.submit_form(url)

"""Call the Main function."""
if __name__ == '__main__':
	s = input("Please input your DigiKey file: ")
	main(s)