def is_between(time, time_range):
    hour_time = int(time.split(':')[0])
    if time_range[1] < time_range[0]:
        return hour_time >= time_range[0] or time <= time_range[1]
    return time_range[0] <= hour_time <= time_range[1]





business_hours = [8, 17]
#if not is_between(timestamp_hours, business_hours):
#    current_diff = current_diff * 0.2
hour1 = '05:00:00'
hour2 = '08:00:00'
hour3 = '14:00:00'
hour4 = '20:00:00'
hour5 = '8:00:00'
print(hour1, is_between(hour1, business_hours))
print(hour2, is_between(hour2, business_hours))
print(hour3, is_between(hour3, business_hours))
print(hour4, is_between(hour4, business_hours))
print(hour5, is_between(hour5, business_hours))