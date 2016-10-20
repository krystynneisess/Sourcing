import csv
import sys
import distributor_cart as dc
import readline

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
				self.board_qty[row[0].lower()] = int(row[1])

	def process_board(self, csv_file):
		"""
		Reads in the specifed board's csv.  
		Then populates distributor_carts accordingly.(See distributor_cart.py for details.)

		Note that a board's bom marts parts from a variety of distributors.
		"""
		# Track current board name for later aggregation
		currBoard = csv_file.replace("_", " ").lower();
		if (currBoard[len(currBoard) - 3:] != "csv"):
			print("%s is not a csv file." % currBoard)
			return
		currBoard = currBoard[0 : len(currBoard) - 4] # truncate the .csv part

		# Read file
		with open(csv_file, 'rt', encoding = 'ISO-8859-1') as f:
			reader = csv.reader(f)
			colNames = next(reader) # Gets row of all the column names
			indexDistributor = 0
			# Finding the index of the distributor column
			for i in range(len(colNames)):
				if colNames[i].lower() == 'distributor':
					indexDistributor = i
					break
			# Populate distributor_carts
			for row in reader:
				dName = row[indexDistributor]
				partNum = row[indexDistributor + 1]
				if dName.lower() == "allied electronics": # Need manufacturer number for URL
					partNum = row[indexDistributor - 1] + "/" + partNum
				# First check if distributor name is already in distributor_carts
				if dName not in self.distributor_carts.keys():
					self.distributor_carts[dName] = dc.DistributorCart(dName) # Create DistributorCart
				# Get the cart object
				dCart = self.distributor_carts[dName]
				dCart_order_qty = dCart.get_qty_dict()
				# Check if part number is already logged
				if partNum not in dCart_order_qty.keys():
					dCart_order_qty[partNum] = 1 * self.board_qty[currBoard]
				else:
					dCart_order_qty[partNum] += 1 * self.board_qty[currBoard]

def main(str):
	auto = BomAutomator()
	files = str.split() # default delimiter is space
	# Read in command-line arguments
	for file in files:
		if file == "board_qty.csv": # Need to initialize board_qty first befoe processing any board
			auto.init_board_qty(file)
	
	for file in files:
		if file != "board_qty.csv":
			auto.process_board(file) # Create distributorCart object for each board
	
	# Create all CSV files
	for cart in auto.distributor_carts:
		auto.distributor_carts[cart].generate_part_number_csv();
		auto.distributor_carts[cart].generate_url_csv();

if __name__ == '__main__':
	"""
	Putting it all together!  

	Something to the effect of:
	- initializing BomAutomator and board_qty
	- process_board() for each board listed in board_qty
	- use DistributorCart methods to output a csv representing each distributor_cart

	"""
	print("Please pass in your board files and board quantity file following these instructions:")
	print("\tAll files should be in the same directory, so you can pass in a file as 'boardName.csv', instead of 'anotherDir/boardName.csv'")
	print("\tThe file containing board quantity is titled 'board_qty.csv'.")
	print("\tThe board files are titled 'boardName.csv', with spaces replaced with underscore, e.g. 'Battery_Buzzer.csv'")
	s = input("Please input your files: ")
	main(s)



	