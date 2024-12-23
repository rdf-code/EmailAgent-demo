import base64
from DatabaseStatus import insert_email
from DatabaseStatus import Status

class EmailReceiver:
    def __init__(self, service):
        self.service = service

    def fetch_latest_email(self):
        results = self.service.users().messages().list(userId='me', labelIds=['INBOX'], q='is:unread', maxResults=1).execute()
        messages = results.get('messages', [])

        if not messages:
            print('No unread emails found.')
            return

        message = messages[0]  # Get the latest message
        msg = self.service.users().messages().get(userId='me', id=message['id'], format='full').execute()
        return msg

    def decode_email(self, msg):
        headers = msg['payload']['headers']
        subject = next(header['value'] for header in headers if header['name'] == 'Subject')
        sender = next(header['value'] for header in headers if header['name'] == 'From')

        part = msg['payload']
        if 'parts' in part:
            part = next(p for p in part['parts'] if p['mimeType'] == 'text/plain')

        body = base64.urlsafe_b64decode(part['body']['data']).decode('utf-8')
        return f"Subject: {subject}\nFrom: {sender}\n\nBody:\n{body}\n"
    
    def save_email_content(self, msg):
            # Extract email details
            headers = msg['payload']['headers']
            subject = next(header['value'] for header in headers if header['name'] == 'Subject')
            sender = next(header['value'] for header in headers if header['name'] == 'From')

            part = msg['payload']
            if 'parts' in part:
                part = next(p for p in part['parts'] if p['mimeType'] == 'text/plain')

            body = base64.urlsafe_b64decode(part['body']['data']).decode('utf-8')

            # Insert email content into the database
            # Assuming initial status is OPEN, modify as needed
            insert_email(sender, subject, body, Status.OPEN)
            print("Email content saved to database.")

