#!/usr/bin/env python

from operator import itemgetter
import sys

current_word = None
current_count = 0
word = None

# input comes from STDIN
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip(',')

    # parse the input we got from mapper.py
    word, count = line.split('\t', 1)

    # convert count (currently a string) to int
    try:
        count = int(count)
    except ValueError:
        # count was not a number, so silently
        # ignore/discard this line
        continue

    # this IF-switch only works because Hadoop sorts map output
    # by key (here: word) before it is passed to the reducer
    if current_word == word:
        current_count += count
    else:
        if current_word:
            # write result to STDOUT
            print '%s\t%s' % (current_word, current_count)
        current_count = count
        current_word = word

# do not forget to output the last word if needed!
if current_word == word:
    print '%s\t%s' % (current_word, current_count)
    
    
    
    
#!/usr/bin/env python

from operator import itemgetter
import sys
import math

temp_cutoff = 5
total_system = 0
total_diff = 0

worst_diff = [-1, -1, -1]
worst_sys = [-1, -1, -1]
for line in sys.stdin:
    
    
    #TODO: actually go through correct stripping/assigning methods
    # remove leading and trailing whitespace
    line = line.strip()

    # parse the input we got from mapper.py
    # word, count = line.split('\t', 1)

    # # convert count (currently a string) to int
    # try:
        # count = int(count)
    # except ValueError:
        # # count was not a number, so silently
        # # ignore/discard this line
        # continue
    
    #first attempt stripping
    # remove leading and trailing whitespace
    line = line.strip()
    # split the line into words
    system_vars = line.split()
    try:
        if len(system_vars) > 0:
            #order_number = system_vars[]
            timestamp_day = system_vars[0]
            timestamp_hours = system_vars[1]
            target_temp = system_vars[2]
            actual_temp = system_vars[3]
            system = system_vars[4]
            age = system_vars[5]
            bldg = system_vars[6]
    except ValueError:
        # improper usage of vars, so silently
        # ignore/discard this line
        continue
    
    
    current_diff = math.abs(temp_actual - temp_target)
    if current_diff < temp_cutoff:
        current_diff = 0

    #is it below or above temp?
    if current_target > current_actual:
        current_diff = current_diff*0.6

    #is it working hours?
    if current_hour < 8 or current_hour > 17:
        current_diff = current_diff * 0.2

    #go through years in service
    current_diff = current_diff * 1/(1-0.4*years/30)
    if years > 10:
        current_diff = current_diff*years/10
    
    if current_system == total_system:
        total_diff = total_diff + current_diff
    else:
        print'%s\t%s' % (total_system, total_diff)
        if total_diff > min(worst_diff):
            min_pos = 0
            for i in range(1, len(worst_diff)):
                if worst_diff[i] < worst_diff[min_pos]:
                    min_pos = i
            worst_diff[min_pos] = total_diff
            worst_sys[min_pos] = total_system
        total_system = current_system
        total_diff = current_diff

#print last case
print'%s\t%s' % (total_system, total_diff)
if total_diff > min(worst_diff):
    min_pos = 0
    for i in range(1, len(worst_diff)):
        if worst_diff[i] < worst_diff[min_pos]:
            min_pos = i
    worst_diff[min_pos] = total_diff
    worst_sys[min_pos] = total_system
total_system = current_system
total_diff = current_diff

#print worst
print'%s\t%s' % (worst_sys[0], worst_diff[0])
print'%s\t%s' % (worst_sys[1], worst_diff[1])
print'%s\t%s' % (worst_sys[2], worst_diff[2])


# program should end here
return 0
        
else:
    temp_diff = temp_actual - temp_target
if time > 8 and time < 17:
    

current_word = None
current_count = 0
word = None

# input comes from STDIN
for line in sys.stdin:
    # remove leading and trailing whitespace
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

    # this IF-switch only works because Hadoop sorts map output
    # by key (here: word) before it is passed to the reducer
    if current_word == word:
        current_count += count
    else:
        if current_word:
            # write result to STDOUT
            print '%s\t%s' % (current_word, current_count)
        current_count = count
        current_word = word

# do not forget to output the last word if needed!
if current_word == word:
    print '%s\t%s' % (current_word, current_count)