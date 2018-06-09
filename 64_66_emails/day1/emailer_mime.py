import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import os


PASSWORD = os.environ['GMAIL_APPLICATION_PASSWORD']
from_addr = 'superyang713@gmail.com'
to_addr = 'superyang713@gmail.com, y.dai@me.com'

msg = MIMEMultipart()
msg['From'] = from_addr
msg['To'] = to_addr
msg['Subject'] = 'New Releases and sales on Steam'

body = """<h1>New Release ans sales on Steam.</h1>

Click the links below to check them out!
"""

msg.attach(MIMEText(body, 'html'))


text = msg.as_string()

smtp_server = smtplib.SMTP('smtp.gmail.com', 587)

smtp_server.ehlo()

smtp_server.starttls()

smtp_server.login('superyang713@gmail.com', PASSWORD)

smtp_server.sendmail(from_addr, to_addr, text)

smtp_server.quit()
print('Email sent successfully')
