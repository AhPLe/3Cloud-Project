#!/usr/bin/env python

#TODO: issue sorting, possibly correct calculation

from operator import itemgetter
import sys

import math
import pandas as pd
import matplotlib.pyplot as plt

def is_between(time, time_range):
    hour_time = int(time.split(':')[0])
    if time_range[1] < time_range[0]:
        return hour_time >= time_range[0] or time <= time_range[1]
    return time_range[0] <= hour_time <= time_range[1]

#temp_cutoff = 2
#total_system = 0
#total_diff = 0
#measured = False

business_hours = [8, 17]

#print('initial')
initiated = False

#print('testing initial system', total_system)
building_array = [[]]
prev_building = -1
pos = -1



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
    
    #split the variables and assign them
    system_vars = line.split('\t')
    
    try:
        if len(system_vars) > 1 and system_vars[0].isdigit():
            
            #print('sys vars', system_vars[5])
            #order_number = system_vars[]
            bldg = int(system_vars[0])
            timestamp_day = system_vars[1]
            timestamp_hours = system_vars[2] #pd.Timestamp()
            actual_temp = int(system_vars[3])
            target_temp = int(system_vars[4])
            system = int(system_vars[5])
            age = int(system_vars[6])
            
            if not is_between(timestamp_hours, business_hours):
                continue
            
            if bldg != prev_building:
                current_timestamp = pd.Timestamp(timestamp_day, timestamp_hours)
                current_building = [bldg, total, bnum, {}]
                building_array.append(current_building)
                prev_building = bldg
                
                if current_timestamp in current_building[3]:
                    current_building[current_timestamp] = [actual_temp, 1]
                else:
                    current_building[current_timestamp][0] += current_building.get(current_timestamp, 0)[0] + actual_temp
                    current_building[current_timestamp][1] += current_building.get(current_timestamp, 0)[1] + 1                    
                pos = pos + 1
            else:
                building_array[pos][1] += actual_temp
                building_array[pos][2] += 1
                
                if current_timestamp in current_building[3]:
                    current_building[current_timestamp] = [actual_temp, 1]
                else:
                    current_building[current_timestamp][0] += current_building.get(current_timestamp, 0)[0] + actual_temp
                    current_building[current_timestamp][1] += current_building.get(current_timestamp, 0)[1] + 1                    
                
        else:
            #print('continuing off of else')
            continue
            
    except ValueError as ve:
        # improper usage of vars, so silently
        # ignore/discard this line
        print('value error', ve)
        continue

hottest_buildings = [1, 2, 3]
hottest_min_pos = 0
hottest_min = 0
#does not work correctly if uneven distribution of measurements
for i in range(len(building_array)):
    if building_array[i][1] > hottest_min:
        hottest_buildings[hottest_min_pos] = i
        hottest_min = building_array[i][1]
        for j in range(len(hottest_buildings)):
            current_building = hottest_buildings[j]
            if building_array[current_building][1] < hottest_min:
                hottest_min_pos = j
                hottest_min = building_array[current_building][1]

hottest_average = []
hottest_times = []
times_measured = False
for i in range(len(hottest_buildings)):
    hottest_average.append([hottest_buildings[i], []]
    for j in range(len(hottest_buildings[3])):
        #get the average for the current time of day
        current_average = hottest_buildings[3][1][0]/hottest_buildings[3][1][1]
        #append the average to the list
        if not times_measured:
            hottest_times.append([hottest_buildings[3][0])
        hottest_average[i][1].append(current_average)
    times_measured = True
    plt.plot(hottest_times, hottest_average[i][2], label = hottest_average[i][0])

plt.xlabel(f'Time (Business Hour)') #  + pd.Timedelta(days=1) - self.small_interval
plt.xticks(rotation=-45)
plt.ylabel('Average Temperature')
plt.title(f'Average Temperature vs. Time')

#plt.savefig('APL_plot.pdf') - used for creating 'plot' figure output
plt.show()
