#!/usr/bin/env python3

import sys # we use this module to access our argument, the 2nd item of the list


argument = sys.argv



# Check all the arguments errors

def negative():
	if int(argument[2]) + abs(int(argument[2])) == 0:
		print("erreur.")
		exit()

def two_args():
	try:
		if argument[2]: 
			pass
	except IndexError:
		print("erreur.")
		exit()

def too_many_arg(): # check if there is a 4th element in argument
	try: 
		if argument[3]:
			print("erreur.")
			exit()
	except IndexError:
		pass


def int_check(a, b):
	try:
		if isinstance(int(a), int) and isinstance(int(b), int):
			pass
	except ValueError:
		print("erreur.")
		exit()

# compute the power of arg1 

def power(a, b):
	if b == 1:
		print(a)
		exit()
	elif b == 0:
		print(1)
		exit()
	else:
		count = 1
		result = a
		while count != b:
			result *= a
			count += 1
		print(result)


negative()
too_many_arg()
two_args()
arg1 = argument[1]
arg2 = argument[2]
int_check(arg1, arg2)
arg1 = int(argument[1])
arg2 = int(argument[2])
power(arg1, arg2)











