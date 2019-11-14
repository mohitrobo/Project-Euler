#counting sundays

from datetime import date
from collections import Counter
import time
start = time.time()

counter = Counter()

for year in range(1901,2001):  #for year in the range
    for month in range(1,13):  #checking for every 1st day of the month
        day = date(year,month,1)
        counter[day.weekday()] += 1

end = time.time()        
print counter[6]  #print number of sundays
print(end-start)
