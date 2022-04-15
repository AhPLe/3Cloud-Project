#!/usr/bin/env python

import sys

# input comes from STDIN (standard input)
for line in sys.stdin:
    #mapper
    
    #print(line)
    line = line.strip()
    # split the line into words
    system_vars = line.split(',')
    #print(system_vars)
    if len(system_vars) > 1 and system_vars[0].isdigit():
        #order_number = system_vars[]
        system = system_vars[0]
        timestamp_day = system_vars[1]
        timestamp_hours = system_vars[2]
        target_temp = system_vars[3]
        actual_temp = system_vars[4]
        age = system_vars[5]
        bldg = system_vars[6]
        
        print '%s\t%s\t%s\t%s\t%s\t%s\t%s' % (system, timestamp_day, timestamp_hours, target_temp, actual_temp, age, bldg)
    else:
        continue
    