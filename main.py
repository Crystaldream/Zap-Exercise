
#############################################
#
# Made by Telmo Reinas
# For Zap
#
# Examples of Usage:
#
# python main.py
# python main.py basket.csv
# python main.py "basket 2.csv"
# python main.py -displayauthors Knu
# python main.py -displayauthors Ker
# python main.py -searchaggregate AAA
# python main.py -searchaggregate USY
#
#############################################

import csv, argparse, re
from books import Book, UsedBook, NewBook, ExclusiveBook
from basket import Basket

parser = argparse.ArgumentParser(description='Book Store')
parser.add_argument('text', action='store', nargs='?', type=str, help='Name of the File: <name.csv>')
parser.add_argument('-displayauthors', action='store', nargs='?', type=str, help='Price with Discounts: <Author>')
parser.add_argument('-searchaggregate', action='store', nargs='?', type=str, help='Search Book By ISBN and Aggregate Multiple Results <isbn capitalized>')
args = parser.parse_args()

asddd = args.text
authors = args.displayauthors
agg = args.searchaggregate

filename = args.text or 'basket.csv'

Basket()
Basket.list.pop(0)
total = 0.00

nw = Basket()
nw.list.pop(0)

def sum_prices(total, li):
	total += float(li)
	return total

def load_file():
	with open(filename, 'r') as f:
		next(f)
		f = csv.reader(f, delimiter=',')
		for r in f:
			"UsedBook" in r[0] and Basket(UsedBook(r[0], r[1], r[2], r[3], r[4]))
			"NewBook" in r[0] and Basket(NewBook(r[0], r[1], r[2], r[3], r[4]))
			"ExclusiveBook" in r[0] and Basket(ExclusiveBook(r[0], r[1], r[2], r[3], r[4]))

file = load_file()

Basket(UsedBook("ExclusiveBook", "AAAGEGEW", "TEST", "10.52", "ZAP"))

l = Basket.list

nw = l
jj = []

for i in l:
	total += float(i.get_price())
	h = authors is not None and authors in i.get_authors() is not ' ' and agg is None and print(i.applyDiscount())
	hh = authors is None and agg is None and filename is not None and print(i.get_book_info())

authors is None and agg is None and print('€ ' + str("%.2f" % round(total, 2)).rjust(2) + ' - Total')

for j in nw:
	vvv = agg is not None and agg in j.get_isbn() and jj.append(j.get_book_info())

size = len(jj)

# the only two direct if conditions in the code:

if size > 0:
	laststr = jj[size-1]
	total_agg = 0.00
	last_str = laststr.split(' ')

	cnt_last = 0

	for ell in last_str:
		cnt_last += 1
		if (bool(re.match("^[.0.-9.]+$", ell))):
			break

	for elem_agg in jj:
		total_agg += float(last_str[cnt_last-1])

	format_last_str = last_str
	format_last_str[cnt_last-1] = str("%.2f" % round(total_agg, 2))
	format_last_str[cnt_last] = '(' + str(size) + ')'

	last = ' '.join(format_last_str)

	print(last)
