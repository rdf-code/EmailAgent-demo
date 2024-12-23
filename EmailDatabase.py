import sqlite3

# Connect to SQLite database (if it doesn't exist, it will be created)
conn = sqlite3.connect('email_info.db')

# Create a cursor object using the cursor() method
cursor = conn.cursor()

# Create table
cursor.execute('''
CREATE TABLE IF NOT EXISTS emails (
    id INTEGER PRIMARY KEY,
    recipient TEXT,
    subject TEXT,
    email_body TEXT,
    status TEXT NOT NULL CHECK( status IN ('Open','Closed','Processing','Special case') )
)
''')

# Commit the transaction
conn.commit()

# Close the connection
conn.close()
