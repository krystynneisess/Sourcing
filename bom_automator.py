import csv
import distributor_cart as dc

class BomAutomator:
	def __init__(self):
		self.distributor_carts = {} # a dictionary mapping distributor names to DistributorCart objects
		self.board_qty = {} # a dictionary mapping a board's name to its quantity

	def get_board_qty(self):
		return self.board_qty

	def get_distributor_carts(self):
		return self.distributor_carts

	def init_board_qty(self, csv_file):
		""" 
		Initializes board_qty based on the contents of board_qty.csv, which contains
		board_name and qty.
		"""
		with open(csv_file, 'rt', encoding = 'ISO-8859-1') as f:
			reader = csv.reader(f)
			colNames = next(reader) # don't need to keep first row
			for row in reader:
				self.board_qty[row[0]] = int(row[1])

	def process_board(self, csv_file):
		"""
		Reads in the specifed board's csv.  
		Then populates distributor_carts accordingly.(See distributor_cart.py for details.)

		Note that a board's bom marts parts from a variety of distributors.
		"""
		with open(csv_file, 'rt', encoding = 'ISO-8859-1') as f:
			reader = csv.reader(f)
			colNames = next(reader)
			indexDistributor = 0
			# Finding the distributor column
			for i in range(len(colNames)):
				if colNames[i].lower() == 'distributor':
					indexDistributor = i
					break
			# Populate distributor_carts
			for row in reader:
				name = row[indexDistributor]
				if name not in self.distributor_carts.keys():
					self.distributor_carts[name] = dc.DistributorCart(name)


if __name__ == '__main__':
	"""
	Putting it all together!  

	Something to the effect of:
	- initializing BomAutomator and board_qty
	- process_board() for each board listed in board_qty
	- use DistributorCart methods to output a csv representing each distributor_cart

	"""
	# Test DistributorCart
	test1 = dc.DistributorCart("sparkfun")
	test1.get_qty_dict()['ppp1'] = 2
	test1.get_qty_dict()['ppp2'] = 3
	test1.get_qty_dict()['ppp3'] = 4
	test1.generate_part_number_csv()
	print(test1.generate_url("HEY8432"))

	# Test BomAutomator
	t2 = BomAutomator()
	t2.init_board_qty('board_qty.csv')
	print(t2.get_board_qty())
	t2.process_board('bom_ex.csv')
	print(t2.get_distributor_carts())

	