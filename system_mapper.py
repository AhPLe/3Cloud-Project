#!/usr/bin/env python

import sys

# input comes from STDIN (standard input)
for line in sys.stdin:
    #mapper
    
    print(line)
    line = line.strip()
    # split the line into words
    system_vars = line.split(',')
    print(system_vars)
    if len(system_vars) > 1 and system_vars[2].isnumeric():
        #order_number = system_vars[]
        timestamp_day = system_vars[0]
        timestamp_hours = pd.Timestamp(system_vars[1])
        target_temp = int(system_vars[2])
        actual_temp = int(system_vars[3])
        system = int(system_vars[4])
        age = int(system_vars[5])
        bldg = int(system_vars[6])
        
        print'%s\t%s\t%s\t%s\t%s\t%s\t%s' % (timestamp_day, timestamp_hours, target_temp, actual_temp, system, age, bldg)
    else:
        continue
    