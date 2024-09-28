import streamlit as st
import google.generativeai as genai

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

for message in st.session_state.chat_history:
    with st.chat_message("User"):
        st.markdown(message)

st.title("🎈 My new Chatbot app")
if prompt := st.text_input("You: ", placeholder="Type your msg"):
    st.session_state.chat_history.append(prompt)
    st.chat_message("User").markdown(prompt)

for message in st.session_state.chat_history:
    st.write(message)