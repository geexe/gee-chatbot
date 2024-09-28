import streamlit as st
import google.generativeai as genai

# Exercise 1.1 – Accepting text input and show the results
# st.write("Create a textbox (st.text_input) to accept the input and display the text (st.write)")
# https://docs.streamlit.io/develop/api-reference/widgets/st.text_input

# ------------------------------------------------------------------------------------------------

# st.title("🐧 My chatbot app")
# # Text input field for the chatbot
# user_input = st.text_input("You: ",placeholder="Type your message here...")

# # Display user input
# if user_input:
#     st.write(f"User Input: {user_input}")


# ------------------------------------------------------------------------------------------------

# Exercise 1.2 – Keep the conversation
# Modify the code so that the app and keep track of the conversation (st.session_state)


# ------------------------------------------------------------------------------------------------

# Display the custom penguin image and title
# st.title("🐧 My chatbot app")
# st.subheader("Conversation")

# # Initialize session state for storing chat history
# if 'chat_history' not in st.session_state:
#     st.session_state.chat_history = []  # Initialize with an empty list

# # Capturing user input and storing messages
# user_input = st.text_input("You:", placeholder="Type your message here...")

# # Append user input to chat history
# if user_input:
#     st.session_state.chat_history.append(user_input)

# # Display all messages in chat history
# for message in st.session_state.chat_history:
#     st.write(message)



# ------------------------------------------------------------------------------------------------

# Exercise 1.3 – Create chat engine
# Use st.chat_message, st.chat_input to create a chat engine
# Chat input box : https://docs.streamlit.io/develop/api-reference/chat/st.chat_input

# ------------------------------------------------------------------------------------------------


# Display the title
# st.title("🐧 My Chatbot App")
# st.subheader("Conversation")

# # Initialize session state for storing chat history
# if 'chat_history' not in st.session_state:
#     st.session_state.chat_history = []  # Initialize with an empty list

# # Create a chat input box
# user_input = st.chat_input("Type your message here ...")

# # If there's input, append it to the chat history
# if user_input:
#     st.session_state.chat_history.append({'role': 'user', 'message': user_input})

# # Display all chat messages in the chat history
# for chat in st.session_state.chat_history:
#     with st.chat_message(chat['role']):
#         st.write(chat['message'])


# ------------------------------------------------------------------------------------------------

# Exercise 1.4 – Add AI to fuel a chat engine
# You can add the ability of Generative AI to enhance your chat engine.
# Chat input box : https://aistudio.google.com/app/apikey

# ------------------------------------------------------------------------------------------------


st.title("🐕 My chatbot app 🐶")
st.subheader("Conversation")

# Capture Gemini API Key
gemini_api_key = st.text_input("Gemini API Key: ", placeholder="Type your API Key here...", type="password")
# Initialize the Gemini Model
if gemini_api_key:
 try:
  # Configure Gemini with the provided API Key
  genai.configure(api_key=gemini_api_key)
  model = genai.GenerativeModel("gemini-pro")
  st.success("Gemini API Key successfully configured.")
 except Exception as e:
  st.error(f"An error occurred while setting up the Gemini model: {e}")
  
# Initialize session state for storing chat history
if "chat_history" not in st.session_state:
 st.session_state.chat_history = [] # Initialize with an empty list
 
# Display previous chat history using st.chat_message (if available)
for role, message in st.session_state.chat_history:
 st.chat_message(role).markdown(message)
 
# Capture user input and generate bot response
if user_input := st.chat_input("Type your message here..."):
 # Store and display user message
 st.session_state.chat_history.append(("user", user_input))
 st.chat_message("user").markdown(user_input)
 
 # Use Gemini AI to generate a bot response
 if model:
  try:
   agent_description = """
    You are a highly effective management coach with expertise in leadership, 
  team dynamics, strategic decision-making, and personal development. Your 
  primary goal is to help individuals become better managers by providing 
  insights, advice, and feedback tailored to their specific challenges.

  Key qualities:
  - Empathetic: You listen carefully to understand the user’s context and offer 
    personalized advice.
  - Actionable: You provide practical, step-by-step guidance that users can apply 
    immediately.
  - Motivational: You encourage users to grow in their leadership roles and inspire 
    confidence.
  - Insightful: You leverage management best practices, offering frameworks and 
    strategies that are backed by experience and research.

  You assist in:
  - Handling team dynamics and conflict resolution
  - Setting and achieving goals
  - Effective communication with direct reports and peers
  - Time management and prioritization
  - Navigating change management and organizational challenges
  - Leading through influence, not just authority

  Maintain a supportive tone, providing constructive feedback while fostering 
  a growth mindset. Use examples and scenarios to help users visualize solutions, 
  and adapt advice based on their industry or role level.

  A manager comes to you with a question:

  """

   context_with_input = f"{agent_description}\n\n{user_input}"
   response = model.generate_content(context_with_input)
   bot_response = response.text
   
   # Store and display the bot response
   st.session_state.chat_history.append(("assistant", bot_response))
   st.chat_message("assistant").markdown(bot_response)
  except Exception as e:
   st.error(f"An error occurred while generating the response: {e}")