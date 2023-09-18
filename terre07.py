#!/usr/bin/env python3
# length of a string
import sys # we use this module to access our argument, the 2nd item of the list


argument = sys.argv


def check_empty():
	try:
		if argument[1]: # try without the len function
			pass
	except IndexError:
		print("erreur.")
		exit()

def check_multi_arg():
	try: 
		if argument[2]:
			print("erreur.")
			exit()
	except IndexError:
		pass
		

def int_check(words):
	try:
		if isinstance(int(words), int):
			print("erreur.")
			exit()
	except ValueError:
		pass

def char_count(characters):
	count = 0
	for char in my_string:
		count += 1
	print(count)



check_empty() # 1. check if we have input an argument
check_multi_arg()
my_string = argument[1]
int_check(my_string) # 2. check if the argument is an integer
char_count(my_string)











