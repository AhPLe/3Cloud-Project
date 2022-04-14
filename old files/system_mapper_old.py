#!/usr/bin/env python

import sys

# input comes from STDIN (standard input)
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()
    # split the line into words
    words = line.split()
    # increase counters
    for word in words:
        # write the results to STDOUT (standard output);
        # what we output here will be the input for the
        # Reduce step, i.e. the input for reducer.py
        #
        # tab-delimited; the trivial word count is 1
        print '%s\t%s' % (word, 1)
		
		
		
#!/usr/bin/env python

import sys

# input comes from STDIN (standard input)
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()
    # split the line into words
    system_vars = line.split(',')
    if len(system_vars) > 0:
        #order_number = system_vars[]
        timestamp_day = system_vars[0]
        timestamp_hours = system_vars[1]
        target_temp = system_vars[2]
        actual_temp = system_vars[3]
        system = system_vars[4]
        age = system_vars[5]
        bldg = system_vars[6]
        
        print'%s\t%s\t%s\t%s\t%s\t%s\t%s' % (timestamp_day, timestamp_hours, target_temp, actual_temp, system, age, bldg)
    else:
        continue
    