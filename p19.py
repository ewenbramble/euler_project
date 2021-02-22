# Project Euler
# Problem 19
# Solution by Ewen Bramble

# Counting Sundays
# How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?

from itertools import cycle

num_days = {'Jan':31,'Feb':28,'Mar':31,'Apr':30,'May':31,'Jun':30,'Jul':31,
            'Aug':31,'Sep':30,'Oct':31,'Nov':30,'Dec':30}
num_days_leap = {'Jan':31,'Feb':29,'Mar':31,'Apr':30,'May':31,'Jun':30,'Jul':31,
            'Aug':31,'Sep':30,'Oct':31,'Nov':30,'Dec':30}
months = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
days = ['Tue','Wed','Thu','Fri','Sat','Sun', 'Mon'] # start with Tue as 1/1/1901 was a Tuesday

sundays_on_first = 0 # count number of Sundays on first day of month

d = cycle(days) # object to loop through list of days
iter_days = iter(d) # iterator object so can stop and resume working through days
    
for year in range(1901,2001):
    if year % 4 != 0: # true if not leap year, use normal month/days dictionary:
        for month in months:
            days_in_month = [] # start each month with empty list to populate with days
            for i in range(num_days[month]):
                days_in_month.append(next(iter_days)) # add days to list using iterator object
            if days_in_month[0] == 'Sun': 
                sundays_on_first += 1 # check if first day of month is a Sunday, if so add to count
    else: # year is leap year so do same but with leap-year dictionary
        for month in months:
            days_in_month = [] 
            for i in range(num_days_leap[month]):
                days_in_month.append(next(iter_days)) 
            if days_in_month[0] == 'Sun': 
                sundays_on_first += 1

print("The number of months between 1901 and 2000 whose first day fell on a Sunday is: {}".format(sundays_on_first))
                