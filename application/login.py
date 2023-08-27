import streamlit as st

def login():

    session_state = st.session_state

    if not session_state.get("Logged in"):
        with st.sidebar:
            st.image("logo.png")
            st.title("Login Here")
            username = st.text_input(
                label="Enter Username",
                placeholder="Username"
            )

            Password = st.text_input(
                label="Enter your Password",
                placeholder="Password",
                type=("password")
            )

            gender =st.radio(
                label="Gender",
                options=["Male","Female"]
            )
            

            if st.button("Login"):
                if username == "admin" and Password == "admin":
                    session_state.username=username
                    session_state["Logged in"] = True
                    session_state.gender = gender
                    st.experimental_rerun()

                elif username != "admin":
                    st.error("Invalid Username",icon="🚫")
                elif Password != "admin":
                    st.error("Invalid Password",icon="🚫")
        st.image("logo.png",width=600)
        st.title("About")
        st.write("Introducing DocuChat: Your interactive document companion powered by LLMS. Upload PDFs, engage in natural language, and let your documents respond. Effortlessly study, research, and explore in a new conversational way!")
        st.markdown("© 2023 NexTech Nexus. All rights reserved.")