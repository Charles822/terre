#!/usr/bin/env python3
# 24H to 12H format converter
import sys # we use this module to access our argument, the 2nd item of the 

argument = sys.argv

time = argument[1]

slice_hours = slice(2) # we isolate the hours as it will be the key item to set our conditions
hours = time[slice_hours]
slice_rest = slice(2,5)
remaining = time[slice_rest] # ":"" + minutes
clock_convert = { # we map the 24H and 12H counterparts 
	
	"13": "01",
	"14": "02",
	"15": "03",
	"16": "04",
	"17": "05",
	"18": "06",
	"19": "07",
	"20": "08",
	"21": "09",
	"22": "10",
	"23": "11",
	"24": "12",
}

# conditions to convert our time
if int(hours) > 12:
	print(f"{clock_convert[hours]}{remaining}PM")
elif int(hours) < 12: 
	print(f"{hours}{remaining}AM")
elif int(hours) == 12:
	print(f"{hours}{remaining}PM")






