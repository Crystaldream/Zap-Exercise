
class Book(object):

	# Constructor
	def __init__(self, type, title, isbn, price, authors):
		self.type = type
		self.title = title
		self.isbn = isbn
		self.price = price
		self.authors = authors

	# Get methods
	def get_type(self):
		return self.type

	def get_title(self):
		return self.title

	def get_isbn(self):
		return self.isbn

	def get_price(self):
		return self.price

	def get_authors(self):
		return self.authors

	# Set functions
	def set_type(self, type):
		self.type = type

	def set_title(self, title):
		self.title = title

	def set_isbn(self, isbn):
		self.isbn = isbn

	def set_price(self, price):
		self.price = format(price, '.2f')

	def set_authors(self, authors):
		self.authors = authors

	# Format authors
	def format_authors(self):
		self.authors = self.authors.replace('|', ', ')

	# Print object
	def get_book_info(self):
		self.format_authors()
		return "€ " + str(format(float(self.price), '.2f')).rjust(6) + ' [' + str(self.get_type()) + '] ' + self.isbn + ': ' + self.title + ' - ' + self.authors

class UsedBook(Book):
	# Polymorfism and Iheritance
	# These three classes inherit from the superclass Book and this method is overwriting the method get_type

	discount = 25

	def get_type(self):
		return 'Usado'

	def applyDiscount(self):
		self.format_authors()
		dis = float(self.price) - ((self.discount*float(self.price))/100)
		return "€ " + str(format(float(self.price), '.2f')).rjust(6) + '/' + str(format(dis, '.2f')) + ': ' + self.title + ' - ' + self.authors

	def get_book_info(self):
		self.format_authors()
		return "€ " + str(format(float(self.price), '.2f')).rjust(6) + ' [' + str(self.get_type()) + '] ' + self.isbn + ': ' + self.title + ' - ' + self.authors

class NewBook(Book):

	discount = 10

	def get_type(self):
		return 'Novo'

	def applyDiscount(self):
		self.format_authors()
		dis = float(self.price) - ((self.discount*float(self.price))/100)
		return "€ " + str(format(float(self.price), '.2f')).rjust(6) + '/' + str(format(dis, '.2f')) + ': ' + self.title + ' - ' + self.authors

	def get_book_info(self):
		self.format_authors()
		return "€ " + str(format(float(self.price), '.2f')).rjust(6) + ' [' + str(self.get_type()) + '] ' + self.isbn + ': ' + self.title + ' - ' + self.authors

class ExclusiveBook(Book):

	discount = 0

	def get_type(self):
		return 'Exclusivo'

	def applyDiscount(self):
		self.format_authors()
		dis = float(self.price) - ((self.discount*float(self.price))/100)
		return "€ " + str(format(float(self.price), '.2f')).rjust(6) + '/' + str(format(dis, '.2f')) + ': ' + self.title + ' - ' + self.authors

	def get_book_info(self):
		self.format_authors()
		return "€ " + str(format(float(self.price), '.2f')).rjust(6) + ' [' + str(self.get_type()) + '] ' + self.isbn + ': ' + self.title + ' - ' + self.authors
