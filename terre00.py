#!/usr/bin/env python3
# print the alphabet in lowcaps

import string # we use this module to import the alphabet letters, our input

alphabet = ""
for letter in string.ascii_letters.lower():
	if letter in alphabet: # to avoid having repeated letters from our input
		continue
	else:
		alphabet += letter
alphabet += "\n"
print (alphabet)










