import csv

class DistributorCart:
	def __init__(self, name):
		distributor_name = name # distributor's name
		order_qty = {} # a dictionary mapping distributor part number to order quantity

	def generate_part_number_csv(self):
		"""
		enerates a csv named "<distributor_name>_url.csv" with rows of the following format:
			<part_quantity>,<part_number>
		"""
		pass
		
	def generate_url(self, part_number):
		"""
		Generates a url for the given part_number.  
		Returns this url as a string.
		"""
		pass

	def generate_url_csv(self): 
		"""
		Generates a csv named "<distributor_name>_url.csv" with rows of the following format:
			<part_quantity>,<part_url>
		"""
		pass
