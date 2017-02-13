"""
Automating shopping cart for Sparkfun orders.
"""
import csv
import time
import os
import readline
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class SparkfunAutomator:
	
	""" Initializes dictionary that maps each URL to its quantity.
	"""
	def __init__(self):
		self.listURLs = {}
		self.driver = None
		self.qtyField = None

	""" Reads in CSV_FILE and puts URLs into listURLs.
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
		self.qtyField = self.driver.find_element_by_class_name("add_qty")
		# Populate quantity in text field
		self.qtyField.send_keys(self.listURLs[url])

	"""Submit shopping cart form.
	"""
	def submit_form(self, url):
		self.driver.find_element_by_class_name("add-cart").click()

"""Processes a Digikey CSV file containing quantity and URL.
"""
def main(fileName):
	automator = SparkfunAutomator()
	# Populate dictionary of URLs
	automator.get_URLs(fileName)
	automator.driver = webdriver.Chrome("C:/Users/Kimberly/Desktop/chromedriver.exe")
	# Fill form for each URL
	for url in automator.listURLs.keys():
		automator.fill_form(url)
		automator.submit_form(url)
	automator.driver.get(automator.driver.current_url)
	# create pop-up
	js = "alert('done')"
	automator.driver.execute_script(js)
	time.sleep(300)

"""Call the Main function."""
if __name__ == '__main__':
	s = input("Please input your Sparkfun CSV file: ")
	main(s)