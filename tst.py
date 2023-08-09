from datetime import datetime as dt

from datetime import timedelta as td


d1 = dt(2023, 7, 1)
d2 = dt.now()
period = d2 - d1
nextday = d1
previous_day = d1 - td(days=1)
for i in range(period.days):
    nextday = previous_day + td(days=1)
    previous_day = nextday
    if nextday.weekday() == 6:
        print("%s is sunday" % nextday)
