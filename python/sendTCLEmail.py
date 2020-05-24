from dotenv import load_dotenv
from email.message import EmailMessage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.header import Header
from email.mime.base import MIMEBase
from email import encoders
from email.mime.application import MIMEApplication
from email.utils import formataddr
from email.utils import make_msgid
from email.utils import formatdate
from os.path import basename
import smtplib
import os
import sys
import datetime
load_dotenv()

def sendEmail(recipient, fullpath):
  EMAIL_ADDRESS = os.getenv("EMAIL_ADDRESS")
  EMAIL_PASSWORD = os.getenv("PASSWORD")

  msg = MIMEMultipart()
  msg['Subject'] = "Sticker Response Data"
  msg['body'] = "This is just a test"
  msg['From'] = EMAIL_ADDRESS
  msg['To'] = recipient

  with open(fullpath, "rb") as fil:
      part = MIMEApplication(
          fil.read(),
          Name=basename(fullpath)
      )
      part['Content-Disposition'] = 'attachment; filename="%s"' % basename(fullpath)
      msg.attach(part)

  with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)

    smtp.send_message(msg)
