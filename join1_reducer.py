#!/usr/bin/env python
import sys

prev_show	= None		#initialize these variabes
total_views = 0			#variable for running total set at 0
print_flag  = 0 		#variable for print set at 0

for line in sys.stdin:
    line       = line.strip()       #strip out carriage return
    key_value  = line.split('\t')   #split line, into key and value, returns a list

    #note: for simple debugging use print statements, ie:  
    curr_show  = key_value[0]         #key is first item in list, indexed by 0
    value_in   = key_value[1]         #value is 2nd item

    if (prev_show != curr_show):
        if (print_flag == 1):
            print('%s\t%s' % (prev_show, total_views))
            print_flag = 0
            total_views = 0
        if (value_in != "ABC"):					# then it's the show views
            (total_views) = int(value_in)		# set total views to value_in
    else:										# prev_show = curr_show
        if (value_in != "ABC"):					# and value is a number
            (total_views) = int(total_views)	# converts to integer
            (value_in)    = int(value_in)		# converts to integer
            (total_views) = (total_views) + (value_in)	# adds view onto running total
    if (value_in == "ABC"):
        print_flag = 1
    prev_show = curr_show	# change prev_show to curr_show

#   	print('%s\t%s' % (curr_show, total_views))

		# Almost_Show should be 50202
#    	print_flag = 0		# reset print_flag to 0
