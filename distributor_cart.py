import csv

class DistributorCart:
	def __init__(self, name):
		self.distributor_name = name # distributor's name
		self.order_qty = {} # a dictionary mapping distributor part number to order quantity

	def get_qty_dict(self):
		return self.order_qty
	
	def generate_part_number_csv(self):
		"""
		Generates a csv named "<distributor_name>_url.csv" with rows of the following format:
			<part_quantity>,<part_number>
		"""
		s = "%s.csv" % (self.distributor_name)
		with open(s, 'a') as x:
			writer = csv.writer(x)
			writer.writerow(["Quantity"], ["Part Number"])
			for part_number in self.order_qty:
				writer.writerow([int(self.order_qty[part_number]), part_number])
		
	def generate_url(self, part_number):
		"""
		Generates a url for the given part_number.  
		Returns this url as a string.
		Looks there are 3 main distributors: DigiKey, AliExpress, Sparkfun, Pololu
		"""
		name = self.distributor_name.lower()
		part_number = str(part_number)
		url = "";
		if name == 'digikey':
			url = "http://www.digikey.com/product-search/en?keywords="
		elif name == 'aliexpress':
			url = "https://www.aliexpress.com/wholesale?catId=0&initiative_id=SB_20161001214135&SearchText="
		elif name == 'sparkfun':
			url = "https://www.sparkfun.com/products/"
			numChars = [49, 50, 51, 52, 53, 54, 55, 56, 57]
			part_number.lstrip("0")
		elif name == 'pololu':
			url = "https://www.pololu.com/product/"
		else:
			return 'Weird distributor'
		return "%s%s" % (url, part_number)

	def generate_url_csv(self): 
		"""
		Generates a csv named "<distributor_name>_url.csv" with rows of the following format:
			<part_quantity>,<part_url>
		"""
		s = "%s_url.csv" % (self.distributor_name)
		with open(s, 'a') as x:
			writer = csv.writer(x)
			writer.writerow(["Quantity"], ["URL"])
			for part in self.order_qty:
				writer.writerow([int(self.order_qty[part]), generate_url(part)])
