import datetime
import pytz

today = datetime.datetime(year=2022, month=5, day=26, hour=13, minute=40, second=0)
tomorrow = datetime.datetime(year=2022, month=5, day=27, hour=13, minute=40, second=0)
print(today)
print(today > tomorrow)
print(datetime.datetime.today())    # no soporta UTC
print(datetime.datetime.now())

today = datetime.datetime.now()
print(today.strftime("%d-%m-%Y"))   # str format time
print(today.strftime("%H:%M"))

user_date = "20-12-1974"
today = datetime.datetime.strptime(user_date, "%d-%m-%Y")   # str parse time
print(today)

# timestamp
# nro seg desde 01-01-1970 00:00:00
today = datetime.datetime.now()
print(today.timestamp())

# timedelta
one_week = datetime.timedelta(days=7)
print(today + one_week)

# timezones
bs_as = pytz.timezone('America/Argentina/Buenos_Aires')

today = datetime.datetime.now(datetime.timezone.utc)
print('utc:', today)
# print(pytz.all_timezones)

local_time = datetime.datetime.now()
print(local_time)
local_time_utc = bs_as.localize(local_time)
print(local_time_utc)

local_time = datetime.datetime.now()
utc_local_time = datetime.datetime.now(tz=pytz.utc)
print(local_time)
print('utc:', utc_local_time)

# HOW TO WORK WITH TZ IN APPs

# Ask users for a local time and their timezone
# Use their timezone to localize the local time
# Convert to UTC before saving to the database
# Always store UTC in your database!

# ejemplo

eastern = pytz.timezone('US/Eastern')

user_date = eastern.localize(datetime.datetime(2020, 4, 15, 6, 0, 0))
print(user_date)
utc_date = user_date.astimezone(pytz.utc)
print(utc_date)     # esta fecha es la que se graba en la BD!

