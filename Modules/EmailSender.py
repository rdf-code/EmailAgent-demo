from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from googleapiclient.errors import HttpError
import base64

class EmailSender:
    def __init__(self, service):
        self.service = service

    def create_message(self, to, subject, message_text):
        """Create a message for an email."""
        message = MIMEMultipart()
        message['to'] = to
        message['subject'] = subject

        msg = MIMEText(message_text)
        message.attach(msg)

        raw_message = base64.urlsafe_b64encode(message.as_bytes())
        raw_message = raw_message.decode()
        return {'raw': raw_message}

    def send_email(self, recipient, subject, body):
        """Send an email."""
        try:
            message = self.create_message(recipient, subject, body)
            sent_message = self.service.users().messages().send(userId="me", body=message).execute()
            print("Message Id: %s" % sent_message['id'])
            return sent_message
        except HttpError as error:
            print(f'An error occurred: {error}')
            return None
