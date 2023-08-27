import streamlit as st
from modules.qa_chain import *
from modules.models import *
from modules.pdf_to_img import *

def display_chat_content():
    chat_history=[]
    # Initialize the session state for chat messages
    if 'chat_messages' not in st.session_state:
        st.session_state.chat_messages = [{"role": "bot", "content": "Hey, how can I help you!", "avatar": "bot.png"}]

    col1, col2, col3 = st.columns([1, 1, 1])
    with col2:
        st.image("chat_pic.png", width=200)

    avatar = None
    for message in st.session_state.chat_messages:
        role = message["role"]
        content = message["content"]
        if role == "bot":
            avatar = "bot.png"
        elif role == "man":
            avatar = "man.png"
        elif role == "woman":
            avatar = "woman.png"
        with st.chat_message(role, avatar=avatar):
            st.write(content)
    user_gender = st.session_state.gender
    if user_gender == "Male":
        role = "man"
    else:
        role = "woman"

    # Take input from the User
    user_input = st.chat_input("Enter a prompt here!")

    # Check if there is user input
    if user_input:
        # Append the user's message to the chat history
        st.session_state.chat_messages.append({"role": role, "content": user_input, "avatar": avatar})
        inputs = {
            'query': user_input,
            'chat_history': chat_history
        }
        st.session_state['user_done']=True


    if st.session_state.get("user_done"):
        message= st.session_state.chat_messages[-1]
        role = message["role"]
        content = message["content"]
        if role == "bot":
            avatar = "bot.png"
            with st.chat_message(role, avatar=avatar):
                st.markdown(content)
        elif role == "man":
            avatar = "man.png"
            with st.chat_message(role, avatar=avatar):
                st.markdown(content)
        elif role == "woman":
            avatar = "woman.png"
            with st.chat_message(role, avatar=avatar):
                st.markdown(content)

        result = (st.session_state.get("qa"))(inputs, return_only_outputs=True)
        chat_history.append((user_input, result["result"]))

        bot_response = result["result"]
        st.session_state.chat_messages.append({"role": "bot", "content": bot_response, "avatar": avatar})

        dic = [result["source_documents"][i].metadata for i in range(len(result["source_documents"]))]
        final_dict = remove_duplicate_dict(dic)
        st.session_state["imgs"] = [convert_pdf_page_to_pil_image(j) for j in final_dict]

        st.session_state['chat']=True
        st.session_state['user_done']=False

    # Display chat messages using Streamlit's built-in chat_message features
    if (st.session_state.get('chat')==True) and (st.session_state.get('user_done')==False):
        message= st.session_state.chat_messages[-1]
        role = message["role"]
        content = message["content"]
       
        avatar = "bot.png"
        with st.chat_message(role, avatar=avatar):
                st.markdown(content)
