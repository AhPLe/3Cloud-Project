#!/usr/bin/env python

import sys
#import pandas as pd

# input comes from STDIN (standard input)
for line in sys.stdin:
    #mapper
    
    #print(line)
    line = line.strip()
    # split the line into words
    system_vars = line.split(',')
    #print(system_vars)
    #empty_data = {'timestamp_day': [], 'timestamp_hours': [], 'actual_temp'}
    #buildings = pd.Dataframe(empty_data)
    if len(system_vars) > 1 and system_vars[6].isdigit():
        #order_number = system_vars[]
        timestamp_day = system_vars[0]
        timestamp_hours = system_vars[1]
        target_temp = system_vars[2]
        actual_temp = system_vars[3]
        system = system_vars[4]
        age = system_vars[5]
        bldg = system_vars[6]
        
        //print (f'%s\t%s\t%s\t%s\t%s\t%s\t%s', bldg, timestamp_day, timestamp_hours, actual_temp, target_temp, system, age))
        print ('%s\t%s\t%s\t%s\t%s\t%s\t%s'.format(bldg, timestamp_day, timestamp_hours, actual_temp, target_temp, system, age))
    
    else:
        continue
    