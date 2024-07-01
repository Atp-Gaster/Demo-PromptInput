import streamlit as st

# Initialize session state for chat history
if 'messages' not in st.session_state:
    st.session_state.messages = []

# Sidebar for user input
st.sidebar.title("Exxon Chatbot template")

# User input form
with st.sidebar.form(key='chat_form'):
    user_message = st.text_input("Your message", "")
    submit_button = st.form_submit_button(label='Send')

# Add user message to chat history and generate a bot response
if submit_button and user_message:
    st.session_state.messages.append({"role": "user", "content": user_message})
    # Simulate a bot response (you can replace this with actual bot logic)
    bot_response = f"{user_message[::-1]}"
    st.session_state.messages.append({"role": "bot", "content": bot_response})
    st.experimental_rerun()

# CSS styles for chat bubbles
st.markdown("""
<style>
.chat-bubble {
    padding: 10px;
    border-radius: 15px;
    margin: 5px;
    max-width: 60%;
    color: black;
}
.user-bubble {
    background-color: #DCF8C6;
    align-self: flex-end;
    text-align: right;
}
.bot-bubble {
    background-color: #ECECEC;
    align-self: flex-start;
}
.chat-container {
    display: flex;
    flex-direction: column;
}
.name {
    font-weight: bold;
    margin-bottom: 5px;
}
</style>
""", unsafe_allow_html=True)

# Display chat messages
st.title("Chat Messages")
chat_container = st.empty()

with chat_container.container():
    for message in st.session_state.messages:
        if message["role"] == "user":
            st.markdown(f"""
            <div class='chat-container' style='align-items: flex-end;'>
                <div class='chat-bubble user-bubble'>
                    <div class='name'>You:</div>
                    {message['content']}
                </div>
            </div>
            """, unsafe_allow_html=True)
        else:
            st.markdown(f"""
            <div class='chat-container' style='align-items: flex-start;'>
                <div class='chat-bubble bot-bubble'>
                    <div class='name'>Bot:</div>
                    {message['content']}
                </div>
            </div>
            """, unsafe_allow_html=True)
