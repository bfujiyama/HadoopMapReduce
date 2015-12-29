#!/usr/bin/env python
import sys

for line in sys.stdin:
    line       = line.strip()   #strip out carriage return
    key_value  = line.split(",")   #split line, into key and value, returns a list
    key_in     = key_value[0]   #key is first item in list
    value_in   = key_value[1]   #value is 2nd item 

    #print key_in
    if (value_in.isdigit()):					#checks if value_in is a number (true)
    	print( '%s\t%s' % (key_in, value_in) )  #print a string, tab, and string
    elif (value_in == "ABC"):
    	print( '%s\t%s' % (key_in, value_in) )  #print a string, tab, and string

#Note that Hadoop expects a tab to separate key value
#but this program assumes the input file has a ',' separating key value
