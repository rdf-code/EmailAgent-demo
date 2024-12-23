import streamlit as st
from APIAgents.OpenAI_Agent import AiAgent  # Import your AiAgent class

# Initialize your AiAgent
ai_agent = AiAgent()

# Title
st.title('OpenAI ChatGPT Integration')

# Input field
user_input = st.text_area("Enter your message", "", height=300)
# Button. It's only enabled when there's some input
if st.button('Send', disabled=(user_input == "")):
    if user_input:
        with st.spinner('Generating response...'):
            # Generate response using your AiAgent
            response = ai_agent.generate_chatgpt_response(user_input)
            
            # Display the response
            #st.text_area("Response", value=response.content, height=200, disabled=True)
            # Display the response with markdown formatting
            st.markdown(response.content, unsafe_allow_html=False)
            # Optional: Clear the input field after sending (commented out, as Streamlit doesn't support clearing inputs yet)
            user_input = " "
    else:
        st.error("Proivde input to get a reply")