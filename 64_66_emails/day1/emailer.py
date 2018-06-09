import smtplib
import os


from_addr = 'superyang713@gmail.com'
to_addr = ['daiy@mit.edu', 'yangdai713.aim.com']
PASSWORD = os.environ['GMAIL_APPLICATION_PASSWORD']

body = """New Release ans sales on Steam.

Click the links below to check them out!
"""
smtp_server = smtplib.SMTP('smtp.gmail.com', 587)

smtp_server.ehlo()

smtp_server.starttls()

smtp_server.login('superyang713@gmail.com', PASSWORD)

smtp_server.sendmail(from_addr, to_addr, body)

smtp_server.quit()
print('Email sent successfully')
