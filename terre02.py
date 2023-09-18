#!/usr/bin/env python3
# Display arguments line by line
import sys # we use this module to access the arguments 

arg_list = sys.argv
arg_list.pop(0) # we remove the first element of the list as it is the filename
for arg in arg_list:
	print(arg)











