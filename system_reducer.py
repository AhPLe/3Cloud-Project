#!/usr/bin/env python

from operator import itemgetter
import sys

import math

# current_word = None
# current_count = 0
# word = None

# # input comes from STDIN
# for line in sys.stdin:
    # # remove leading and trailing whitespace
    # line = line.strip(',')

    # # parse the input we got from mapper.py
    # word, count = line.split('\t', 1)

    # # convert count (currently a string) to int
    # try:
        # count = int(count)
    # except ValueError:
        # # count was not a number, so silently
        # # ignore/discard this line
        # continue

    # # this IF-switch only works because Hadoop sorts map output
    # # by key (here: word) before it is passed to the reducer
    # if current_word == word:
        # current_count += count
    # else:
        # if current_word:
            # # write result to STDOUT
            # print '%s\t%s' % (current_word, current_count)
        # current_count = count
        # current_word = word

# # do not forget to output the last word if needed!
# if current_word == word:
    # print '%s\t%s' % (current_word, current_count)
    
    
    
    
#!/usr/bin/env python

def is_between(time, time_range):
    # if time_range[1] < time_range[0]:
        # return time >= time_range[0] or time <= time_range[1]
    return time_range[0] <= time <= time_range[1]

temp_cutoff = 2
total_system = 0
total_diff = 0
measured = False

worst_diff = [-1, -1, -1]
worst_sys = [-1, -1, -1]

#print('initial')
lines = lines[1:]
testing_sys = int(lines[0].strip().split(',')[5])
total_system = testing_sys

#print('testing initial system', total_system)

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
    
    #split the varialbes and assign them
    system_vars = line.split(',')
    
    try:
        if len(system_vars) > 1 and system_vars[3].isnumeric():
            #print('sys vars', system_vars[5])
            #order_number = system_vars[]
            timestamp_day = system_vars[1]
            timestamp_hours = pd.Timestamp(system_vars[2])
            target_temp = int(system_vars[3])
            actual_temp = int(system_vars[4])
            system = int(system_vars[5])
            age = int(system_vars[6])
            bldg = int(system_vars[7])
            
        else:
            #print('continuing off of else')
            continue
            
            
            
    except ValueError as ve:
        # improper usage of vars, so silently
        # ignore/discard this line
        print('value error', ve)
        continue
    
    current_diff = abs(actual_temp - target_temp)
    # print('target temp', target_temp)
    # print('actual temp', actual_temp)
    # print('diff temp', current_diff)
    #print('total sys', total_system, total_diff)
    if current_diff < temp_cutoff:
        current_diff = 0

    #is it below or above temp?
    if target_temp > actual_temp:
        current_diff = current_diff*0.6

    #is it working hours?
    #if timestamp_hours < datetime.time(8) or timestamp_hours > datetime.time(17):
    #df.timestamp.dt.strftime('%H:%M:%S').between('8:00:00','17:00:00')
    #    current_diff = current_diff * 0.2
    

    
    # print(timestamp_hours)
    # print(timestamp_hours.strftime('%H:%M:%S'))
    # print(is_between(timestamp_hours.strftime('%H:%M:%S'), ['08:00:00','17:00:00']))
    
    #go through years in service
    current_diff = current_diff * 1/(1-0.4*age/30)
    if age > 10:
        current_diff = current_diff*age/10
    
    if system == total_system:
        total_diff = total_diff + current_diff
    else:
    
        #print('%s\t%s', total_system, total_diff)

        if total_diff > min(worst_diff):
            
            min_pos = 0
            for i in range(1, len(worst_diff)):
                if worst_diff[i] < worst_diff[min_pos]:
                    min_pos = i
            #print('replacing', min_pos)
            worst_diff[min_pos] = total_diff
            worst_sys[min_pos] = total_system

    total_system = system
    total_diff = current_diff

#print('post')
#print last case
#print('%s\t%s', total_system, total_diff)
if total_diff > min(worst_diff):
    min_pos = 0
    for i in range(1, len(worst_diff)):
        if worst_diff[i] < worst_diff[min_pos]:
            min_pos = i
    worst_diff[min_pos] = total_diff
    worst_sys[min_pos] = total_system

#print worst
print('worst prints')
print'%s\t%s' % (worst_sys[0], worst_diff[0])
print'%s\t%s' % (worst_sys[1], worst_diff[1])
print'%s\t%s' % (worst_sys[2], worst_diff[2])