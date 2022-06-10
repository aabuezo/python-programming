"""
If you get an SMTPAuthenticationError even when your password is correct,
it's possible that you have 2-factor authentication enabled.
You'll need to use an App Password to log in instead of your normal password.

If you don't have 2-FA enabled, you'll have to allow acces by
less secure apps in your Gmail security preferences-though remember to deactivate
it once you've finished learning about sending e-mails with Python!
"""
import os
import smtplib

from dotenv import load_dotenv
from email.message import EmailMessage


load_dotenv()
EMAIL = os.environ.get("EMAIL")
PASS = os.environ.get("PASS")
TO = os.environ.get("TO")


email = EmailMessage()
email['Subject'] = 'Test email'
email['From'] = EMAIL
email['To'] = TO
email.set_charset("Test email sent from Python!")

smtp_connector = smtplib.SMTP(host='smtp.gmail.com', port=587)
smtp_connector.starttls()
smtp_connector.login(EMAIL, PASS)

smtp_connector.send_message(email)
smtp_connector.quit()