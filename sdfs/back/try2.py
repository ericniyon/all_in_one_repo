import datetime


def next_day(given_date, weekday):
    days_ahead = (weekday - given_date.weekday()) 
    if days_ahead <= 0: # Target day already happened this week
        days_ahead += 7
    return now + datetime.timedelta(days_ahead)

now = datetime.date.today()



print( next_day(now,4))

#     return given_date + datetime.timedelta(days=day_shift)

# now = datetime.date(2019, 12, 19) 

# for weekday in range(7):
