import streamlit as st
from application.login import *
from application.main import *
from application.chat import *
from application.evidence import *

login()

if st.session_state.get("Logged in"):
    if not st.session_state.get("processed"):
        file_upload()

    if st.session_state.get("processed"):
        read_docs()


    if st.session_state.get("chain_created"):
        qa = st.session_state.get("qa")
        display_chat_content()


    if st.session_state.get("chat"):
        show_evidence(st.session_state.get("imgs"))