# OpenAI & Google API Wrapper Demo

In this simple project, I'm using OpenAI and Google API to create an agent that can receive emails and respond to them.

My goal is to highlight the potential of using AI to automate and customize email processing and responses.

I've separated the code into modules for clarity and reusability.

The main.py file is the entry point for the application. It initializes the Google API client, fetches the latest email, and processes it using the OpenAI agent.

The EmailReceiver module handles the interaction with the Google API to fetch and process emails.

The EmailSender module handles the interaction with the Google API to send emails.

The AiAgent module handles the interaction with the OpenAI API to process the email content and generate a response.

The DatabaseStatus module handles the interaction with the SQLite database to store and retrieve email statuses.

The test_app.py file is a simple Streamlit app that displays the email data from the SQLite database.

I've also included a requirements.txt file to list the dependencies for the project.

I hope this project inspires you to explore the possibilities of using AI to automate and customize email processing and responses.



