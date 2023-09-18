#!/usr/bin/env python3

import sys # we use this module to access our argument
from math import floor

argument = sys.argv

arg1 = int(argument[1])
arg2 = int(argument[2])


# Avoid division by 0
if arg2 == 0:
	print("erreur.") 
	exit()

division = floor(arg1 / arg2)
if division == 0: # print a custom erreur if the result of the div is 0 (3 / 5 is not a mathematical error)
	print("erreur.") 
	exit()
reste = arg1 % arg2


print(f"Résultat: {division}")
print(f"Reste: {reste}")








