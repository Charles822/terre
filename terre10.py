#!/usr/bin/env python3
# Prime number or not
import sys # we use this module to access our argument, the 2nd item of the 

argument = sys.argv

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

def int_check(x):
	try:
		if isinstance(int(x), int):
			pass
	except ValueError:
		print("erreur.")
		exit()


def check_empty():
	try:
		if argument[1]: # try without the len function
			pass
	except IndexError:
		print("erreur.")
		exit()

def prime(arg):
	a = 0
	b = 0
	if arg == 1:
		print(f"Non, {arg} n'est pas un nombre premier")
		exit()
# we want to check if we find any combination of numbers in a range excluding 1 and our argument that would be equal to our argument
	for num1 in range(2,arg):  
		if a * b != arg:
			a = num1
		for num2 in range(2,arg):
			if a * b != arg:
				b = num2 
	if a * b == arg: # if we find one, then our argument is not a prime number. If we don't, it is! 
		print(f"Non, {arg} n'est pas un nombre premier")		
	else:
		print(f"Oui, {arg} est un nombre premier")


check_empty()
arg = argument[1]
int_check(arg)
check_negative()
too_many_arg()
arg = int(argument[1])
prime(arg)






