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
    
        TODO: actually go through correct stripping/assigning methods
    remove leading and trailing whitespace
    line = line.strip()

    # parse the input we got from mapper.py
    word, count = line.split('\t', 1)

    # convert count (currently a string) to int
    try:
        count = int(count)
    except ValueError:
        # count was not a number, so silently
        # ignore/discard this line
        continue
    