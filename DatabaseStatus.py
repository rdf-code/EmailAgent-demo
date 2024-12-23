from enum import Enum
import sqlite3

class Status(Enum):
    OPEN = "Open"
    CLOSED = "Closed"
    PROCESSING = "Processing"
    SPECIAL_CASE = "Special case"


def insert_email(recipient, subject, email_body, status):
    conn = sqlite3.connect('email_info.db')
    cursor = conn.cursor()
    # Convert enum to string value
    status_value = status.value
    cursor.execute('''
    INSERT INTO emails (recipient, subject, email_body, status) 
    VALUES (?, ?, ?, ?)
    ''', (recipient, subject, email_body, status_value))
    conn.commit()
    conn.close()

def update_email_status(email_id, new_status):
    conn = sqlite3.connect('email_info.db')
    cursor = conn.cursor()

    cursor.execute('UPDATE emails SET status = ? WHERE id = ?', (new_status.value, email_id))
    conn.commit()

    conn.close()
