import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
from app.utils.contest_confirmation import template
import ssl

ssl._create_default_https_context = ssl._create_unverified_context

def send_mail(to_email):
    message = Mail(
        from_email = "contest@pixelmath.org",
        to_emails = to_email,
        subject = "Successfully Signed Up for PixelMath Contest!",
        html_content = template
    )
    try:
        sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
        response = sg.send(message)
    except Exception as e:
        raise e
