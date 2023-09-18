#!/usr/bin/env python3
# # compute the square root of a number without using the built in function
import sys # we use this module to access our argument, the 2nd item of the 
from math import floor

argument = sys.argv


def check_empty():
	try:
		if argument[1]: # try without the len function
			pass
	except IndexError:
		print("erreur.")
		exit()

def check_negative():
	if int(argument[1]) != 0 and int(argument[1]) + abs(int(argument[1])) == 0:
		print("erreur.")
		exit()

def too_many_arg(): # check if there is a 3rd element in the argument list
	try: 
		if argument[2]:
			print("erreur.")
			exit()
	except IndexError:
		pass

def int_check(a):
	try:
		if isinstance(int(a), int):
			pass
	except ValueError:
		print("erreur.")
		exit()

def square_root(number):
	x = 0
	while floor(x * x) != number:
		x += 0.00001
	print(round(x))

if argument[1] == 0:
	print(0)
	exit()
check_empty()
arg = argument[1]
int_check(arg)
check_negative()
too_many_arg()
arg = int(argument[1])
square_root(arg)









