import smtplib
from functools import wraps
import os


def main():
    pass


def attach_to_gmail(sender=None, recipients=None, password=None):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            text = func(*args, **kwargs)
            smtp_server = smtplib.SMTP('smtp.gmail.com', 587)
            smtp_server.ehlo()
            smtp_server.starttls()
            smtp_server.login(sender, password)
            smtp_server.sendmail(sender, recipients, text)
            smtp_server.quit()
            print('Email sent successfully')

        return wrapper
    return decorator


if __name__ == '__main__':
    main()
