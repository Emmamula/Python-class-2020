#1.  current time.
import sys
import datetime

data = datetime.datetime.now().time()
print("current time:")
print(data)
print("")

  data = line.strip().split("\t")
     if len(data) == 6:
         date, time, store, item, cost, payment = data

     print("{0}\t{1}\t{2}".format(item, cost, time))

#2.  Add the timedelta to the datetime and subtract 60 seconds and add 2 years
from datetime import timedelta
from datetime import datetime
print("Add 2 years and subtract 60 seconds:")
print(datetime.now() - timedelta(seconds=60) + timedelta(days=730))
print("")

#3. Create a timedelta object representing 100 days, 10 hours, and 13 minutes.
d = timedelta(days = 100, hours = 10, minutes = 13)
(d.days, d.seconds, d.microseconds)
(-1, 86399, 999999)
print("Object representing 100 days, 10 hours, and 13 minutes:")
print(d)
print("")

# 4. Write a function that takes two arguments (feet and inches) with this time object. I used walking. 
>>>def distance():
    print("Input walking distance:")
    ft = int(input("Feet: "))
    inch = int(input("Inches: "))
    inch += ft*12
    miles = inch/63360
    #avg walking pace is 3.1 mph
    time_h = round(miles/3.1, 2)
    print("It'll take the average human " + str(time_h) + " hour(s) to walk that distance.")

    time2 = datetime.now() + timedelta(hours=time_h)
    print("If you leave now, you'll get there at " + str(time2))

distance()
