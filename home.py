import streamlit as st

st.set_page_config(
    page_title="Versatile Leader Assistant",
    layout="wide",
    menu_items={
        'About': "https://isitnet.com"
    })


st.header("Hello,")
st.subheader("How can I assist you today?")
st.text("")
st.markdown("Here are some suggestions to get you started")

if "user_initial_prompt" not in st.session_state:
    st.session_state['user_initial_prompt'] = ""

input = st.chat_input("Ask a Question",key="chat_ask_question")

if st.button("Who is a Versatile Leader", use_container_width=True):
    st.session_state['user_initial_prompt'] = "Who is a Versatile Leader"
    st.switch_page("pages/chat.py")

if st.button("What is Influence", key="button2", use_container_width=True):
    st.session_state['user_initial_prompt'] = "What is Influence"
    st.switch_page("pages/chat.py")

if st.button("What is the Physician Metaphor", key="button3", use_container_width=True):
    st.session_state['user_initial_prompt'] = "What is the Physician Metaphor"
    st.switch_page("pages/chat.py")

if input:
    st.session_state['user_initial_prompt'] = input
    st.switch_page("pages/chat.py")
    