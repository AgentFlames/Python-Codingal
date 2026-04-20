import random
import time

def getrandomdate(startdate,enddate):
    randomgenerator = random.random()
    dateformat = "%d/%m/%Y"

    starttime = time.mktime(time.strptime(startdate,dateformat))
    endtime = time.mktime(time.strptime(enddate,dateformat))

    randomtime = starttime + randomgenerator * (endtime-starttime)
    randomdate = time.strftime(dateformat,time.localtime(randomtime))
    return randomdate

print("Random date is", getrandomdate("1/1/2026", "31/12/2026"))