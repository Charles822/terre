#!/usr/bin/env python3

import sys # we use this module to access our argument

# find Switzerland (the middle value in a series of 3 numbers)

argument = sys.argv

a = int(argument[1]) 
b = int(argument[2]) 
c = int(argument[3]) 

my_nums = [a, b, c]


# not very elegant but it works 

if a == b and b == c : 
	print("erreur.")
elif a == b and c > a: 
	print("erreur.")
elif b == c and a > b: 
	print("erreur.")
elif a == c and b > a: 
	print("erreur.") 
elif a < b and b < c: 
	print(b)
elif b < a and a < c : 
	print(a)
elif a < c and c < b: 
	print (c) 
elif a == b and c < a: 
	print(c)
elif b == c and a < b: 
	print(a)
elif  a == c and b < a: 
	print(b) 






