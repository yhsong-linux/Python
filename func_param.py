#!/usr/bin/python3.1
# Filename : func_params.py

def printmax(a, b):
	if a > b:
		print(a)
	else:
		print(b)

printmax(3, 4)

x = int(input('Please input the value of x : '))
y = int(input('Please input the value of y : '))
printmax(x, y)
