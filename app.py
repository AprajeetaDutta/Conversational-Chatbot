import streamlit as st
from chatbot import ChatBot

st.title("Conversational Chatbot")

bot = ChatBot()

if 'chat_history' not in st.session_state:
    st.session_state['chat_history'] = []

user_input = st.text_input("You: ", "")

if user_input:
    response = bot.ask(user_input)
    st.session_state['chat_history'].append((user_input, response))

if st.session_state['chat_history']:
    for chat in st.session_state['chat_history']:
        st.write(f"You: {chat[0]}")
        st.write(f"Bot: {chat[1]}")
