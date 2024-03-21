import streamlit as st

st.set_page_config(
    page_title="Versatile Leader Assistant",
    layout="wide",
    menu_items={
        'About': "https://isitnet.com"
    })
st.title("Hello,")
st.header("How can I assist you today?")
st.text("")
st.text("")
st.text("")
st.markdown("Here are some suggestions to get you started")
col1, col2, col3 = st.columns(3, gap="small")

with col1:
    if st.button('Who is a Versatile Leader', use_container_width=True):
        if "user_initial_prompt" not in st.session_state:
            st.session_state['user_initial_prompt'] = "Who is a Versatile Leader"
        st.switch_page("pages/chat.py")

with col2:
    if st.button('What is the meaning of Influence', use_container_width=True):
        if "user_initial_prompt" not in st.session_state:
            st.session_state['user_initial_prompt'] = "What is Influence"
        st.switch_page("pages/chat.py")

with col3:
    if st.button('Explain the Physician Metaphor', use_container_width=True):
        if "user_initial_prompt" not in st.session_state:
            st.session_state['user_initial_prompt'] = "Explain Physician Metaphor"
        st.switch_page("pages/chat.py")

if st.button('What metaphor can I use when my company is in Decline', use_container_width=True):
        if "user_initial_prompt" not in st.session_state:
            st.session_state['user_initial_prompt'] = "What metaphor can I use when my company is in Decline"
        st.switch_page("pages/chat.py")

col1, col2 = st.columns(2, gap="small")

with col1:
    if st.button('What are the business lifecycle stages', use_container_width=True):
        if "user_initial_prompt" not in st.session_state:
            st.session_state['user_initial_prompt'] = "What are the business lifecycle stages"
        st.switch_page("pages/chat.py")

with col2:
    if st.button('How can I be a good Manager', use_container_width=True):
        if "user_initial_prompt" not in st.session_state:
            st.session_state['user_initial_prompt'] = "How to be a good Manager"
        st.switch_page("pages/chat.py")


input = st.chat_input("Ask a Question",key="chat_ask_question")

st.markdown("""
    <style>
        section[data-testid="stSidebar"][aria-expanded="true"]{
            display: none;
        }
        div[data-testid="StyledLinkIconContainer"]{
            font-family: "Montserrat", sans-serif;
        }
        div[data-testid="stMarkdownContainer"]{
            font-family: "Montserrat", sans-serif;
        }
        input[aria-label="Ask a Question"]{
            font-size: larger;
            font-family: "Montserrat", sans-serif;
        }
        textarea[data-testid="stChatInputTextArea"]{
            font-size: larger;
            font-family: "Montserrat", sans-serif;
        }
        .st-bz {
          max-height: none;
          border-radius: 50px;
        }
        .element-container st-emotion-cache-1exz1qz e1f1d6gn4 {
          position: absolute;
          bottom: 0px;
          right: 3rem;
          display: none
        }
        .st-emotion-cache-f4ro0r {
          display: flex;
          align-items: flex-end;
          height: 100%;
          position: absolute;
          right: 0px;
          pointer-events: none;
          display: none;
        }
        .st-emotion-cache-s1k4sy {
          background-color: transparent;
          position: relative;
          -webkit-box-flex: 1;
          flex-grow: 1;
          border-radius: 50px;
          display: flex;
          -webkit-box-align: center;
          align-items: center;
        }
        .stChatInput {
          border-radius: 50px;
          display: flex;
          background-color: rgb(240, 242, 246);
        }
        
        .st-emotion-cache-1wrcr25 {
          display: flex;
          flex-direction: row;
          -webkit-box-pack: start;
          place-content: flex-start;
          -webkit-box-align: stretch;
          align-items: stretch;
          position: absolute;
          inset: 0px;
          overflow: hidden;
        }
        .st-b7 {
            background-color: rgb(240, 242, 246);
            padding: 10px;
            margin-right: 20px;
            border-radius: 50px;
        }
        .st-emotion-cache-1li7dat {
            font-size: 12px;
            color: rgba(49, 51, 63, 0.6);
            margin: 0px;
            text-align: right;
            position: absolute;
            bottom: 0px;
            right: 7px;
            display: none;
        }
        .stTextInput {
            position: fixed;
            bottom: 50px;
        }
        @media only screen and (max-width: 768px) {
            div[data-baseweb="textarea"]{
                outline: none;
                padding: 5px;
                border-radius: 50px;
            }
            .st-b4 {
                outline: none;
                padding: 5px;
                border-radius: 50px;
            }
            /** For Chat Input Section **/
            .st-emotion-cache-1wm93xv {
                width: 100%;
                padding: 1rem 1rem 55px;
                min-width: auto;
                max-width: initial;
            }
            /** For Chat History Section **/
            .st-emotion-cache-9tg1hl {
                width: 100%;
                padding: 6rem 1rem 1rem;
                min-width: auto;
                max-width: initial;
            }
            .block-container {
                width: 100%;
            }
            .st-emotion-cache-1umgz6k {
                display: inline-flex;
                -webkit-box-align: center;
                align-items: center;
                -webkit-box-pack: center;
                justify-content: center;
                font-weight: 400;
                padding: 0.25rem 0.75rem;
                border-radius: 0.5rem;
                min-height: 38.4px;
                margin: 0px;
                line-height: 1.6;
                color: inherit;
                width: 100%;
                user-select: none;
                padding: 5px;
                background-color: rgb(255, 255, 255);
                border: 1px solid rgba(49, 51, 63, 0.2);
            }
        }
        @media only screen and (max-width: 910px) {
            div[data-baseweb="textarea"]{
                outline: none;
                padding: 5px;
                border-radius: 50px;
            }
            .st-b4 {
                outline: none;
                padding: 5px;
                border-radius: 50px;
            }
            /** For Chat Input Section **/
            .st-emotion-cache-1wm93xv {
                width: 100%;
                padding: 1rem 1rem 55px;
                min-width: auto;
                max-width: initial;
            }
            /** For Chat History Section **/
            .st-emotion-cache-9tg1hl {
                width: 100%;
                padding: 6rem 1rem 1rem;
                min-width: auto;
                max-width: initial;
            }
            .block-container {
                width: 100%;
            }
            .st-emotion-cache-1umgz6k {
                display: inline-flex;
                -webkit-box-align: center;
                align-items: center;
                -webkit-box-pack: center;
                justify-content: center;
                font-weight: 400;
                padding: 0.25rem 0.75rem;
                border-radius: 0.5rem;
                min-height: 38.4px;
                margin: 0px;
                line-height: 1.6;
                color: inherit;
                width: 100%;
                user-select: none;
                padding: 10px;
                background-color: rgb(255, 255, 255);
                border: 1px solid rgba(49, 51, 63, 0.2);
            }
        }
        @media only screen and (min-width: 910px) {
            div[data-baseweb="textarea"]{
                outline: none;
                padding: 5px;
                border-radius: 50px;
            }
            .st-b4 {
                outline: none;
                padding: 5px;
                border-radius: 50px;
            }
            /** For Chat Input Section **/
            .st-emotion-cache-1wm93xv {
                width: 100%;
                padding: 1rem 1rem 55px;
                min-width: auto;
                max-width: initial;
            }
            .block-container {
                width: 100%;
            }
            .st-emotion-cache-1umgz6k {
                display: inline-flex;
                -webkit-box-align: center;
                align-items: center;
                -webkit-box-pack: center;
                justify-content: center;
                font-weight: 400;
                padding: 0.25rem 0.75rem;
                border-radius: 0.5rem;
                min-height: 38.4px;
                margin: 0px;
                line-height: 1.6;
                color: inherit;
                width: 100%;
                user-select: none;
                padding: 5px;
                background-color: rgb(255, 255, 255);
                border: 1px solid rgba(49, 51, 63, 0.2);
            }
        }
        @media only screen and (min-width: 1024px) {
            div[data-baseweb="textarea"]{
                outline: none;
                padding: 10px;
                border-radius: 50px;
            }
            .st-b4 {
                outline: none;
                padding: 10px;
                border-radius: 50px;
            }
            /** For Chat Input Section **/
            .st-emotion-cache-1wm93xv {
                width: 50%;
                padding: 1rem 1rem 55px;
                min-width: auto;
                max-width: initial;
            }
            .block-container {
                width: 50%;
            }
            .st-emotion-cache-1umgz6k {
                display: inline-flex;
                -webkit-box-align: center;
                align-items: center;
                -webkit-box-pack: center;
                justify-content: center;
                font-weight: 400;
                padding: 0.25rem 0.75rem;
                border-radius: 0.5rem;
                min-height: 38.4px;
                margin: 0px;
                line-height: 1.6;
                color: inherit;
                width: 100%;
                user-select: none;
                padding: 25px;
                background-color: rgb(255, 255, 255);
                border: 1px solid rgba(49, 51, 63, 0.2);
            }
        }
        
    </style>
    """, unsafe_allow_html=True)

if input:
    if "user_initial_prompt" not in st.session_state:
        st.session_state['user_initial_prompt'] = input
    st.switch_page("pages/chat.py")
    