import datetime


inputNum = int(input())
d = datetime.datetime(year=2022, month=7, day=2, hour=21)

print((d + datetime.timedelta(minutes=inputNum)).strftime('%H:%M'))
