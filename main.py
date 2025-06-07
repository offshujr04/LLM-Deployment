import streamlit as st
import google.generativeai as genai

api_key = st.secrets["API_KEY"]
# api_key = 'AIzaSyDJyAUgbBfPVzGnKgrNB0Llqm7IFn4q-x8'
genai.configure(api_key=api_key) 

model = genai.GenerativeModel('gemini-1.5-flash')

st.set_page_config(
    page_title="AI Chatbot",
    layout="centered"   
)

# st.markdown(
#     """
#     <style>
#     .stApp {
#         background-color: #000000;
#         color:white;
#     }
#     </style>
#     """,unsafe_allow_html=True
# )

st.markdown("""
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    </style>
""", unsafe_allow_html=True)

st.title("AI Chatbot")

# Chat history
if "chat" not in st.session_state:
    st.session_state.chat = model.start_chat(history=[])
    st.session_state.messages = []

for msg in st.session_state.messages:
    st.chat_message(msg["role"]).markdown(msg["content"])

# User input
user_input = st.chat_input("You:")

if user_input: 
    # Display user message
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)
    

    response = st.session_state.chat.send_message(user_input)
    bot_reply = response.text
    st.session_state.messages.append({"role": "assistant", "content": bot_reply})
    with st.chat_message("assistant"):
        st.markdown(bot_reply)
    # Response
    # st.chat_message("assistant").markdown(response.text)