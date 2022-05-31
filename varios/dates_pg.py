import datetime
import pytz
import psycopg2
import os
from dotenv import load_dotenv

load_dotenv()

conn = psycopg2.connect(os.environ.get('DATABASE_URI'))

user_timezone = pytz.timezone("America/Argentina/Buenos_Aires")

new_post_content = input('Enter what you learned today: ')

new_post_date = user_timezone.localize(datetime.datetime.now())
utc_post_date = new_post_date.astimezone(pytz.utc)

with conn:
    with conn.cursor() as cursor:
        cursor.execute("INSERT INTO posts (content, date) VALUES (%s, %s);",
                       (new_post_content, utc_post_date.timestamp()))
        