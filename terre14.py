#!/usr/bin/env python3
# check if numbers are in the right order without using the sort function
import sys 

my_numbers = sys.argv[1:]


def check_int(list):
	try:
		for num in my_numbers:
			if isinstance(int(num), int):
				pass
	except ValueError:
		print("erreur.")
		exit()


def check_trie(list):
	for i in range(0, len(my_numbers) - 1): 
		if int(my_numbers[i]) <= int(my_numbers[i + 1]):
			continue
		else:
			print("Pas Triée !")
			exit()
	print("Triée !")


check_int(my_numbers)
check_trie(my_numbers)






