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
            color: lightgray;
            caret-color: lightgray;
        }
        textarea[data-testid="stChatInputTextArea"]{
            font-size: larger;
            font-family: "Montserrat", sans-serif;
            color: black;
            caret-color: red;
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
          background-color: #1E1F20;
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
            background-color: #1E1F20;
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
        button[data-testid="baseButton-secondary"]{
            padding: 20px;
        }
        
        @media only screen and (max-width: 768px) {
            div[data-baseweb="textarea"]{
                outline: none;
                padding: 5px;
                border-radius: 50px;
                background-color: #1E1F20;
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
        }
        @media only screen and (max-width: 910px) {
            div[data-baseweb="textarea"]{
                outline: none;
                padding: 5px;
                border-radius: 50px;
                background-color: #1E1F20;
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
        }
        @media only screen and (min-width: 910px) {
            div[data-baseweb="textarea"]{
                outline: none;
                padding: 5px;
                border-radius: 50px;
                background-color: #1E1F20;
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
        }
        @media only screen and (min-width: 1024px) {
            div[data-baseweb="textarea"]{
                outline: none;
                padding: 10px;
                border-radius: 50px;
                background-color: #1E1F20;
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
        }
        
    </style>
    """, unsafe_allow_html=True)

if input:
    st.session_state['user_initial_prompt'] = input
    st.switch_page("pages/chat.py")
    