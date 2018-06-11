from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import os

from gmail import attach_to_gmail


PASSWORD = os.environ['GMAIL_APPLICATION_PASSWORD']
sender = 'superyang713@gmail.com'
recipients = ['y.dai@me.com', 'superyang713@gmail.com']


def main():
    subject = 'This is a test'
    body = """None"""
    template_file = 'email.html'

    email_setup(sender,
                recipients,
                subject,
                body=body,
                template_file=template_file,
                body_format='html',
                external_template=True)


@attach_to_gmail(sender=sender, recipients=recipients, password=PASSWORD)
def email_setup(sender, recipients, subject, template_file=None, body=None,
                body_format='plain', external_template=True,):
    msg = MIMEMultipart()
    msg['From'] = sender
    msg['To'] = ', '.join(recipients)
    msg['Subject'] = subject
    if external_template is False:
        msg.attach(MIMEText(body, body_format))
    else:
        with open(template_file) as fin:
            text = fin.read()
            msg.attach(MIMEText(text, body_format))

    return msg.as_string()


if __name__ == '__main__':
    main()
