import streamlit as st
from chatbot import chatbot, context


st.set_page_config(
    page_title="CLAT 2025 Assistant",
    page_icon="📚",
    layout="centered"
)

st.title("CLAT 2025 Assistant")
st.markdown("""
This chatbot will help you with information about CLAT 2025 (Common Law Admission Test), 
including exam pattern, eligibility criteria, preparation tips, and more.
""")


if "messages" not in st.session_state:
    st.session_state.messages = []
    

if "conversation_history" not in st.session_state:
    st.session_state.conversation_history = []


if "example_question" not in st.session_state:
    st.session_state.example_question = None


def set_example_question(question):
    st.session_state.example_question = question


for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])


def process_user_input(user_question):
    
    st.session_state.messages.append({"role": "user", "content": user_question})
    st.session_state.conversation_history.append(("user", user_question))
    
    
    with st.chat_message("user"):
        st.markdown(user_question)
    
    
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            
            response = chatbot(user_question, context)
            st.markdown(response)
    
    
    st.session_state.conversation_history.append(("ai", response))
    
    
    st.session_state.messages.append({"role": "assistant", "content": response})


with st.sidebar:
    st.header("Example Questions")
    example_questions = [
        "What is CLAT?",
        "When is CLAT 2025 expected to be held?",
        "What is the eligibility criteria for CLAT?",
        "How many questions are there in the English section?",
        "What are the best books for CLAT preparation?",
        "What is the exam pattern for CLAT 2025?",
        "How should I prepare for the logical reasoning section?",
        "What are the top NLUs in India?",
        "Is there negative marking in CLAT?",
        "What is the application process for CLAT 2025?"
    ]
    
    for question in example_questions:
        if st.button(question, key=f"btn_{question}"):
            set_example_question(question)
    
    st.markdown("---")
    st.markdown("### CLAT 2025 Resources")
    st.markdown("- [Official CLAT Website](https://consortiumofnlus.ac.in/)")
    st.markdown("- [Previous Year Papers](https://consortiumofnlus.ac.in/clat-2025/)")
    st.markdown("- [CLAT Preparation Guide](https://www.lawctopus.com/clat/)")

# Process example question if one was selected
if st.session_state.example_question:
    question = st.session_state.example_question
    st.session_state.example_question = None  # Reset after processing
    process_user_input(question)

# User input field
user_question = st.chat_input("Ask me about CLAT 2025...")

# If user submits a question
if user_question:
    process_user_input(user_question)