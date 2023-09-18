#!/usr/bin/env python3

import sys # we use this module to access our argument, the 2nd item of the 

# transform 12H format into 24H format 

argument = sys.argv

time = argument[1]

slice_hours = slice(2) # we isolate the hours as it will be the key item to set our conditions
hours = time[slice_hours]
slice_rest = slice(2,5)
remaining = time[slice_rest] # ":"" + minutes
slice_meridian = slice(5,7)
meridian = time[slice_meridian]
clock_convert = { # we map the 24H and 12H counterparts 
	
	"01": "13",
	"02": "14",
	"03": "15",
	"04": "16",
	"05": "17",
	"06": "18",
	"07": "19",
	"08": "20",
	"09": "21",
	"10": "22",
	"11": "23",
	"12": "12",
}

# conditions to convert our time
if meridian == "PM":
	print(f"{clock_convert[hours]}{remaining}")
elif meridian == "AM": 
	print(f"{hours}{remaining}")







