import datetime

x = datetime.datetime.today()

tdy = datetime.date.toordinal(x)

past = datetime.date.toordinal(datetime.date(2020,5,31))

print(tdy)

print(past)

print(tdy - past)
