import datetime
from datetime import timedelta


startingx  = datetime.date(2019,11,1)
endingy = startingx + timedelta(days=51)
fy = endingy

print(fy)

if endingy:
    startingx = endingy - timedelta(days=21)
    ending = startingx + timedelta(days=35 ,hours=17, minutes=55)
    if ending!=True:
        print(startingx)
        print(ending)







