#!/usr/bin/python3.1
# Filename : func_doc.py

def printmax(x, y):
	'''Prints the maximum of two numbers.
	The two values must be integers.'''

	x = int(x)
	y = int(y)
	
	if x > y:
		print(x, 'is maximum')
	else:
		print(y, 'is maximum')

printmax(3, 5)
print(printmax.__doc__)
