# This file contains the functions used to test
# if condition specified in automations.json for a
# given automation are satisfied.

# Functions like time_day_only return a binary result (0/1)
# while other functions (like temperature_check) return a range (e.g. 0,1,2)
# of codes, specific to the service they are used with.

from datetime import datetime


def time_day_only(days='days', time_on='time_on', time_off='time_off'):
    
    # defines current time
    now = datetime.now()
    now = datetime.strftime(now, "%H:%M")

    # defines weekday
    weekday = datetime.today().weekday()
 
    #checks if times are during the same day

    if time_off >= time_on:
        # if time_off >= time_on (e.g. 01:20 --> 17:45)
        # both times are part of the same day

        # checks current time is in desired range
        if time_on <= now <= time_off:
            if (weekday) in days:
                return 1
    else:
        # if time_off <= time_on (e.g. 17:45 --> 01:20)
        # both times are part of different days

        # check if time is before midnight
        if time_on <= now <= '23:59':
            if (weekday) in days:
                return 1

        # check if time is after midnight, accounting
        # for difference in the weekday
        elif '00:00' <= now <= time_off:
            # calculates previous day of the week
            whole_week = [0,1,2,3,4,5,6]
            yesterday = whole_week[weekday-1 % len(whole_week)]
            if (yesterday) in days:
                return 1  
    return 0

def temperature_check(days='days', time_on='time_on', time_off='time_off', min_temp='min_temp', max_temp='max_temp', temp='temp'):
    # code 1 is ON, code 2 is OFF

    if time_day_only(days, time_on, time_off):
        if min_temp <= temp < max_temp:
            return 1
    else:
        return 2

