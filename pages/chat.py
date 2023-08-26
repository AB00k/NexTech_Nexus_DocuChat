import streamlit as st
from modules.qa_chain import *
from modules.models import *
from modules.pdf_to_img import *

def display_chat_content():
    chat_history = []

    col1,col2,col3=st.columns([1,1,1])
    with col2:
        st.image("chat_pic.png",width=200)

    avatar=None
    # Initialize the session state for chat messages
    if 'chat_messages' not in st.session_state:
        st.session_state.chat_messages = [{"role": "bot", "content": "How can I help you?"}]
        st.session_state['chat']=True
    user_gender=st.session_state.gender
    if user_gender == "Male":
        role = "man"
    else:
        role = "woman"
    
    #Take input from the User
    user_input=st.chat_input("Enter a prompt here!",key="user_input")

    # Check if there is user input
    if user_input:
        # Append the message with the role, content, and avatar
        st.session_state.chat_messages.append({"role": role, "content": user_input, "avatar": avatar})
        inputs = {
            'query': user_input,
            'chat_history': chat_history
        }

        result = (st.session_state.get("qa"))(inputs, return_only_outputs=True)
        chat_history.append((user_input, result["result"]))
        print_chat()

        st.experimental_rerun()
    
    bot_response = result["result"]
    st.session_state.chat_messages.append({"role": "bot", "content": bot_response, "avatar": avatar})
    print_chat()

    dic = [result["source_documents"][i].metadata for i in range(len(result["source_documents"]))]
    final_dict = remove_duplicate_dict(dic)

    st.session_state["imgs"] = [convert_pdf_page_to_pil_image(j) for j in final_dict]

    # Display chat messages using Streamlit's built-in chat_message features
def print_chat():
    for msg in st.session_state.chat_messages:
        if msg["role"]=="bot":
            avatar="bot.png"
        if msg["role"]=="man":
            avatar="man.png"
        if msg["role"]=="woman":
            avatar="woman.png"
        with st.chat_message(msg["role"], avatar=avatar):
            st.markdown(msg["content"])