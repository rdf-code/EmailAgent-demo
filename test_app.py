import streamlit as st
import sqlite3
import pandas as pd

# Function to connect to the SQLite database and fetch data
def load_data():
    conn = sqlite3.connect('email_info.db')
    query = "SELECT * FROM emails"
    df = pd.read_sql_query(query, conn)
    conn.close()
    return df

# Load data from the database
data = load_data()

# Display the data in Streamlit
st.write("Data from SQLite database:", data)
