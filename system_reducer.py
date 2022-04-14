#!/usr/bin/env python

#TODO: issue sorting, possibly correct calculation

from operator import itemgetter
import sys

import math
#import pandas as pd

def is_between(time, time_range):
    hour_time = int(time.split(':')[0])
    if time_range[1] < time_range[0]:
        return hour_time >= time_range[0] or time <= time_range[1]
    return time_range[0] <= hour_time <= time_range[1]

temp_cutoff = 2
total_system = 0
total_diff = 0
measured = False

worst_diff = [-1, -1, -1]
worst_sys = [-1, -1, -1]
business_hours = [8, 17]

#print('initial')
initiated = False

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
    system_vars = line.split('\t')
    
    try:
        if len(system_vars) > 1 and system_vars[3].isdigit():
            
            #print('sys vars', system_vars[5])
            #order_number = system_vars[]
            timestamp_day = system_vars[0]
            timestamp_hours = system_vars[1] #pd.Timestamp()
            target_temp = int(system_vars[2])
            actual_temp = int(system_vars[3])
            system = int(system_vars[4])
            age = int(system_vars[5])
            bldg = int(system_vars[6])
            if not initiated:
                initiated = True
                testing_sys = system
            
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
    business_hours = ['8', '17']
    if not is_between(timestamp_hours, business_hours):
        current_diff = current_diff * 0.2
    

    
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
