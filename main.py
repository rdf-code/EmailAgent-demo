from APIAgents.OpenAI_Agent import AiAgent
from APIAgents.GoogleAPI_Agent import GoogleAgent
from Modules.EmailReceiver import EmailReceiver
from Modules.EmailSender import EmailSender
from DatabaseStatus import update_email_status
from DatabaseStatus import Status
import sqlite3
def get_email_details(email_id, new_status):
    conn = sqlite3.connect('email_info.db')
    cursor = conn.cursor()

    cursor.execute('SELECT recipient, subject FROM emails WHERE id = ?', (email_id,))
    details = cursor.fetchone()
    cursor.execute('UPDATE emails SET status = ? WHERE id = ?', (new_status.value, email_id))
    conn.close()
    return details

        
def get_first_open_email():
    conn = sqlite3.connect('email_info.db')
    cursor = conn.cursor()

    # Retrieve the first 'OPEN' email
    cursor.execute('SELECT * FROM emails WHERE status = ? ORDER BY id ASC LIMIT 1', (Status.OPEN.value,))
    email = cursor.fetchone()

    conn.close()
    return email

def main():
    print("Creating GoogleAgent instance...")
    googleAgent = GoogleAgent("C:\\code\\MailAgent\\api_keys\\client_secret_73573224486-5nabsjj6h7rscd7lpoocl3aml8dq4vch.apps.googleusercontent.com.json", ['https://www.googleapis.com/auth/gmail.modify'])
    
    print("Creating EmailReceiver instance")
    email_Receiver = EmailReceiver(googleAgent.service)
    email_Sender = EmailSender(googleAgent.service) 
    print("Creating AiAgent instance...")
    openaiAgent = AiAgent()
    
    print("Fetching the latest email...")
    msg = email_Receiver.fetch_latest_email()
    
    if msg:
        print("Decoding email content...")
        #email_content = email_Receiver.decode_email(msg)
        
        print("Saving email content...")
        email_Receiver.save_email_content(msg)
    else:
        print("No unread emails found or an error occurred.")

    first_open_email = get_first_open_email()
    if first_open_email:
        email_id = first_open_email[0]
        email_body = first_open_email[3]
        print("Generating response with OpenAI...")
        response = openaiAgent.generate_chatgpt_response(email_body)
        print("Response from OpenAI:", response.content)
        recipient, original_subject = get_email_details(email_id,Status.PROCESSING)
        reply_subject = f"Re: {original_subject}"
        sent_message = email_Sender.send_email(recipient, reply_subject, response.content)
        print(sent_message)
        if sent_message:
            update_email_status(email_id, Status.CLOSED)
            print("Email sent and status updated to 'Closed'.")
        else:
            print("Failed to send email.")

if __name__ == "__main__":
    main()
