import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

def send_estimate_email(to_email, subject, html_content):
    api_key = os.getenv("SENDGRID_API_KEY")
    if not api_key:
        raise Exception("SENDGRID_API_KEY not set")
    message = Mail(
        from_email="noreply@priceestimator.com",
        to_emails=to_email,
        subject=subject,
        html_content=html_content
    )
    sg = SendGridAPIClient(api_key)
    response = sg.send(message)
    return response.status_code
