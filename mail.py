import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import os


def send_mail(receiver, subject, message):

    me = "boyuan@boyuan12.me"
    password = os.getenv("EMAIL_PASSWORD")

    msg = MIMEMultipart("alternative")
    msg["Subject"] = subject
    msg["From"] = me
    msg['To'] = receiver

    html = message
    part2 = MIMEText(html, 'html')

    msg.attach(part2)

    s = smtplib.SMTP_SSL("mail.privateemail.com")
    s.login(me, password)
    s.sendmail(me, receiver, msg.as_string())
    s.quit()

