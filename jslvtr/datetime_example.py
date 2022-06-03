from datetime import datetime, timezone, timedelta

# naive time object: no information about timezone
print(datetime.now())


today = datetime.now(timezone.utc)
tomorrow = today + timedelta(days=1)
print(today)
print(tomorrow)


# string format time
print(today.strftime('%d-%m-%Y %H:%M:%S'))

# string parse time
another_date = '2018-03-01'
print(datetime.strptime(another_date, '%Y-%m-%d'))
