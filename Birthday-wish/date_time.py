import datetime as dt

now = dt.datetime.now()

if now.year == 2021:
    print('yes')

date_of_birth = dt.datetime(year=1997,month=3,day=27)

print(date_of_birth)

print(now.date())