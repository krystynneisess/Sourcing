import csv
import distributor_cart

class BomAutomator:
	def __init__(self):
		distributor_carts = {} # a dictionary mapping distributor names to DistributorCart objects
		board_qty = {} # a dictionary mapping a board's name to its quantity

	def init_board_qty(self):
		""" 
		Initializes board_qty based on the contents of board_qty.csv.
		"""
		pass

	def process_board(self, board_name):
		"""
		Reads in the specifed board's csv.  
		Then populates distributor_carts accordingly.  (See distributor_cart.py for details.)

		Note that a board's bom marts parts from a variety of distributors.
		"""
		pass

if __name__ == '__main__':
	"""
	Putting it all together!  

	Something to the effect of:
	- initializing BomAutomator and board_qty
	- process_board() for each board listed in board_qty
	- use DistributorCart methods to output a csv representing each distributor_cart

	"""
	pass
	