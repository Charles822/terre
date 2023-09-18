#!/usr/bin/env python3

import sys # we use this module to access our argument


argument = sys.argv


def int_check(number):
	try:
		if not isinstance(int(my_number), int):
			pass
	except ValueError:
		print("Tu ne me la mettra pas à l’envers")
		exit()

def odd_or_even(number):
	if my_number % 2 == 0:
		print("pair")
	elif my_number % 2 != 0:
		print("impair")


def check_empty():
	if len(argument) == 1: 
		print("Tu ne me la mettra pas à l’envers")
		exit()
	else:
		return

check_empty() # 1. check if we have input an argument
my_number = argument[1]
int_check(my_number) # 2. check if the argument is an integer
my_number = int(argument[1])
odd_or_even(my_number) # 3. check if the number is odd or even via mod









