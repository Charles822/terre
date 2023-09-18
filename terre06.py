#!/usr/bin/env python3

import sys # we use this module to access our argument

def too_many_arg(): # check if there is a 3rd element in the argument list
	try: 
		if argument[2]:
			print("erreur.")
			exit()
	except IndexError:
		pass


def check_empty():
	try:
		if argument[1]: # try without the len function
			pass
	except IndexError:
		print("erreur.")
		exit()


argument = sys.argv


check_empty()
too_many_arg()


my_string = argument[1]


i = -1 # set i to fetch the value of the last character of our string
my_string_length = len(my_string) + 1 # the total number of characters in our string + 1 to fulfil our while loop condition
result = ""

while abs(i) != my_string_length: # condition to go through all the items of our input in reverse
	result += my_string[i]
	i -= 1


print(result)











