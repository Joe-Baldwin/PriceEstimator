import os
import sys
import json
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

def handle_send_email(to_email, subject, html_content):
    api_key = os.getenv("SENDGRID_API_KEY")
    if not api_key:
        return {'error': 'SENDGRID_API_KEY not set'}
    message = Mail(
        from_email="noreply@priceestimator.com",
        to_emails=to_email,
        subject=subject,
        html_content=html_content
    )
    sg = SendGridAPIClient(api_key)
    response = sg.send(message)
    return {'status': response.status_code}

def main():
    print("SendGrid MCP server started")
    sys.stdout.flush()
    for line in sys.stdin:
        try:
            request = json.loads(line)
            action = request.get('action')
            if action == 'send_email':
                to_email = request['to_email']
                subject = request['subject']
                html_content = request['html_content']
                result = handle_send_email(to_email, subject, html_content)
                print(json.dumps(result))
            else:
                print(json.dumps({'error': 'Unknown action'}))
        except Exception as e:
            print(json.dumps({'error': str(e)}))
        sys.stdout.flush()

if __name__ == "__main__":
    main()
