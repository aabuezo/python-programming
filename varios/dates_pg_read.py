import datetime
import pytz
import psycopg2
import os
from dotenv import load_dotenv

load_dotenv()

conn = psycopg2.connect(os.environ.get('DATABASE_URI'))

user_timezone = pytz.timezone("America/Argentina/Buenos_Aires")

with conn:
    with conn.cursor() as cursor:
        cursor.execute("SELECT * FROM posts")
        for post in cursor:
            _id, content, timestamp = post
            naive_datetime = datetime.datetime.utcfromtimestamp(timestamp)
            utc_date = pytz.utc.localize(naive_datetime)
            local_date = utc_date.astimezone(user_timezone)
            print(local_date)
            print(content)
