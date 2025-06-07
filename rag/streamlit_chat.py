import streamlit as st
from manage_chroma_db import run_query

st.set_page_config(page_title="Sales Copilot", page_icon="🤖")
st.title("🤖 KinetEco Chatbot")

# Initialize session state for chat history
if "history" not in st.session_state:
    st.session_state.history = []

# Chat input
query = st.chat_input("Ask a question about KinetEco EVs:")

if query:
    st.session_state.history.append(("user", query))
    answer, _ = run_query(query)
    st.session_state.history.append(("assistant", answer))

# CSS
st.markdown("""
<style>
.chat-container {
    display: flex;
    margin-bottom: 1rem;
}
.bot {
    justify-content: flex-start;
}
.user {
    justify-content: flex-end;
}
.bubble {
    max-width: 75%;
    padding: 0.75rem 1rem;
    border-radius: 1rem;
    line-height: 1.5;
    font-size: 1rem;
}
.bot .bubble {
    background-color: #e1f5fe;
    border-top-left-radius: 0;
}
.user .bubble {
    background-color: #f1f0f0;
    border-top-right-radius: 0;
}
.avatar {
    font-size: 1.5rem;
    margin: 0 0.5rem;
    align-self: flex-end;
}
</style>
""", unsafe_allow_html=True)

# Display chat history
for speaker, message in st.session_state.history:
    if speaker == "assistant":
        st.markdown(f"""
        <div class="chat-container bot">
            <div class="avatar">🤖</div>
            <div class="bubble">{message}</div>
        </div>
        """, unsafe_allow_html=True)
    else:
        st.markdown(f"""
        <div class="chat-container user">
            <div class="bubble">{message}</div>
            <div class="avatar">🧑</div>
        </div>
        """, unsafe_allow_html=True)