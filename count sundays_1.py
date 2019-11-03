#counting sundays

from datetime import date
from collections import Counter

counter = Counter()

for year in range(1901,2001):  #for year in the range
    for month in range(1,13):  #checking for every 1st day of the month
        day = date(year,month,1)
        counter[day.weekday()] += 1

print counter[6]
