import streamlit as st
import openai

# Set up OpenAI API key
openai.api_key = "YOUR_OPENAI_API_KEY"

# Page Configuration
st.set_page_config(page_title="DOJ Virtual Assistant", page_icon="⚖️", layout="centered")

# App Title
st.title("Department of Justice Virtual Assistant ⚖️")
st.markdown("Welcome! Ask your questions, and I'll do my best to help you.")

# Initialize session state for conversation history
if "messages" not in st.session_state:
    st.session_state["messages"] = []

# Function to communicate with OpenAI API
def ask_openai(question):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=question,
        max_tokens=150,
        temperature=0.5,
    )
    return response.choices[0].text.strip()

# Chat input
user_input = st.text_input("You:", "", placeholder="Ask me anything about DOJ...")

# Check for user input
if user_input:
    # Append user's message to conversation history
    st.session_state.messages.append({"role": "user", "content": user_input})

    # Get response from OpenAI
    response = ask_openai(user_input)
    st.session_state.messages.append({"role": "assistant", "content": response})

    # Clear user input
    user_input = ""

# Display conversation history
for message in st.session_state.messages:
    if message["role"] == "user":
        st.markdown(f"**You:** {message['content']}")
    else:
        st.markdown(f"**Assistant:** {message['content']}")

# Sidebar for additional information
st.sidebar.title("About")
st.sidebar.info(
    "This virtual assistant is designed to help answer questions related to the Department of Justice. "
    "Type your questions in the chat box to get started."
)
