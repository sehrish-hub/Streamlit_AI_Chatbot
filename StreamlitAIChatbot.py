# import streamlit as st
# import google.generativeai as genai
# import os
# from dotenv import load_dotenv
# from datetime import datetime

# #  Load environment variables from .env file
# load_dotenv()

# #  Fetch API key securely from environment variables
# GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# if GEMINI_API_KEY:
#     genai.configure(api_key=GEMINI_API_KEY)  #  Only configure if API key exists
# else:
#     st.error("API key not found! Please check your .env file.")

# #  Custom CSS for professional UI
# st.markdown(
#     """
#     <style>
#         .main {
#             background: linear-gradient(to right, #1f4037, #99f2c8);
#             color: white;
#         }
#         .chat-container {
#             padding: 10px;
#             border-radius: 10px;
#             background-color: rgba(255, 255, 255, 0.1);
#             margin: 10px 0;
#         }
#         .user-msg {
#             color: #0f0;
#             font-weight: bold;
#         }
#         .ai-msg {
#             color: #00f;
#             font-weight: bold;
#         }
#         .stButton>button {
#             background-color: #ff9800;
#             color: white;
#             border-radius: 8px;
#             padding: 10px 20px;
#             border: none;
#         }
#     </style>
#     """,
#     unsafe_allow_html=True,
# )

# st.title("🤖 AI Chatbot")
# st.write("Ask anything!")

# #  Initialize session state for chat history
# if "chat_history" not in st.session_state:
#     st.session_state.chat_history = []

# #  User input field
# user_input = st.chat_input("Enter your message...")

# if user_input:  #  When user submits a message
#     try:
#         if "time" in user_input.lower():
#             ai_response = f"The current time is {datetime.now().strftime('%I:%M %p')}"
#         else:
#             model = genai.GenerativeModel("gemini-pro")
#             response = model.generate_content(user_input)
#             ai_response = response.text

#         #  Store conversation properly as a list of formatted strings
#         st.session_state.chat_history.append(f"User: {user_input}")
#         st.session_state.chat_history.append(f"AI: {ai_response}")

#     except Exception as e:
#         st.error(f"Error: {e}")

# #  Display chat history with better UI
# st.subheader("🤖 Chat History:")
# for msg in st.session_state.chat_history:
#     st.markdown(f'<div class="chat-container">{msg}</div>', unsafe_allow_html=True)
import streamlit as st
import google.generativeai as genai
import os
from dotenv import load_dotenv
from datetime import datetime

# Load environment variables
load_dotenv()

# Fetch API key
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

if not GEMINI_API_KEY:
    st.error("API key not found! Please check your .env file.")
    st.stop()  # Stop execution if API key is missing

# Configure Gemini AI
genai.configure(api_key=GEMINI_API_KEY)

# Use correct model
model_name = "gemini-1.5-pro"  # Updated model name

st.title("🤖 AI Chatbot")
st.write("Ask anything!")

# Initialize chat history
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# User input
user_input = st.chat_input("Enter your message...")

if user_input:
    try:
        if "time" in user_input.lower():
            ai_response = f"The current time is {datetime.now().strftime('%I:%M %p')}"
        else:
            model = genai.GenerativeModel(model_name)
            response = model.generate_content(user_input)
            ai_response = response.text if hasattr(response, "text") else "No response received."

        # Store chat history
        st.session_state.chat_history.append(f"User: {user_input}")
        st.session_state.chat_history.append(f"AI: {ai_response}")

    except Exception as e:
        st.error(f"Error: {e}")

# Display chat history
st.subheader("🤖 Chat History:")
for msg in st.session_state.chat_history:
    st.write(msg)
    
