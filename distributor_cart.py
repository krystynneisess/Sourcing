import csv
import sys
import re

class DistributorCart:
	def __init__(self, name):
		self.distributor_name = name # distributor's name
		self.order_qty = {} # a dictionary mapping distributor part number to order quantity
		# Save all the distributor site URLs
		self.distributor_urls = {}
		self.distributor_urls["digikey"] = ("http://www.digikey.com/product-detail/en/", "")
		self.distributor_urls["allied electronics"] = ("http://www.alliedelec.com/anderson-power-products-", "")
		self.distributor_urls["sparkfun"] = ("https://www.sparkfun.com/products/", "https://www.waytekwire.com/item/", "/")
		# The distributors below do not have shopping cart automators as of 1/28/17.
		self.distributor_urls["waytek"] = ("https://www.waytekwire.com/item/", "/")
		self.distributor_urls["aliexpress"] = ("https://www.aliexpress.com/wholesale?catId=0&initiative_id=SB_20161001214135&SearchText=", "")
		self.distributor_urls["hobbyking"] = ("http://www.hobbyking.com/hobbyking/store/RC_PRODUCT_SEARCH.asp?strSearch=", "")
		self.distributor_urls["amazon"] = ("https://www.amazon.com/s/ref=nb_sb_noss?url=search-alias%3Daps&field-keywords=", "")

	def get_qty_dict(self):
		return self.order_qty
	
	def generate_part_number_csv(self):
		"""
		Generates a csv named "<distributor_name>_url.csv" with rows of the following format:
			<part_quantity>,<part_number>
		"""
		s = "%s.csv" % (self.distributor_name)
		with open(s, 'a') as x:
			writer = csv.writer(x, lineterminator = '\n')
			writer.writerow(["Quantity", "Part Number"])
			for part_number in self.order_qty:
				if "/" in part_number:
					writer.writerow([int(self.order_qty[part_number]), part_number[part_number.index("/") + 1:]])
				else:
					writer.writerow([int(self.order_qty[part_number]), part_number])
		
	def generate_url(self, part_number):
		"""
		Generates a url for the given part_number.  
		Returns this url as a string.
		"""
		name = self.distributor_name.lower()
		part_number = str(part_number)
		url = "";
		if name not in self.distributor_urls.keys():
			print(self.order_qty)
			sys.exit("We currently cannot generate URL for %s" % name)
		else:
			if name == "sparkfun":
				part_number = part_number[4:].strip("0") # need to strip the 0s for URL
			distributor = self.distributor_urls[name]
			url = distributor[0] + part_number + distributor[1]
			re.sub(" \t\n\r", "", url)
		return "%s" % (url)

	def generate_url_csv(self): 
		"""
		Generates a csv named "<distributor_name>_url.csv" with rows of the following format:
			<part_quantity>,<part_url>
		"""
		s = "%s_url.csv" % (self.distributor_name)
		with open(s, 'a') as x:
			writer = csv.writer(x, lineterminator = '\n')
			writer.writerow(["Quantity", "URL"])
			for part in self.order_qty:
				writer.writerow([int(self.order_qty[part]), self.generate_url(part)])
