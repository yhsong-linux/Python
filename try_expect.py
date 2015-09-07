#!/usr/bin/python3.1
# Filename: try_except.py

import sys

try:
	s = input('Enter something --> ')
except EOFError:
	print('\nWhy did you do an EOF on me?')
	sys.exit()
except:
	print('\nSome error/exception occurred.')

print('Done')
