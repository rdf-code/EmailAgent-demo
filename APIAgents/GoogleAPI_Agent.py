import base64
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

class GoogleAgent:
    def __init__(self, api_key_path, scopes):
        self.service = self.get_gmail_service(api_key_path,scopes)

    def get_gmail_service(self, api_key_path, scopes):
        flow = InstalledAppFlow.from_client_secrets_file(api_key_path, scopes=scopes)
        credentials = flow.run_local_server(port=0)
        return build('gmail', 'v1', credentials=credentials)