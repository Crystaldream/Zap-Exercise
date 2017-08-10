
class Basket(object):

	list = []

	# Constructor
	def __init__(self, Book=[]):
		self.list.append(Book)

	def __repr__(self):
		self.list = []

	# Get functions
	def get_book(id):
		return list[id]

	def get_book_list():
		return list

	# Set functions
	def set_book(self, Book):
		self.list.append(Book)

	def set_book_list(self, list):
		self.list = list
