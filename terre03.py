#!/usr/bin/env python3

import string # we use this module to import the alphabet letters
import sys # we use this module to access the arguments 


argument = sys.argv
my_letter = argument[1].lower()
alphabet = string.ascii_lowercase


for letter in alphabet:
	if letter != my_letter:
		alphabet = alphabet.replace(letter, "")
	else:
		break
print(alphabet)	









