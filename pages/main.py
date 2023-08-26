import streamlit as st
import os
from modules.vectordb import *
from modules.qa_chain import *
from modules.models import *


def file_upload():
    with st.sidebar:
        st.title("Dashboard")
        files=st.file_uploader(
            "Upload a pdf or a Zip Document",
            type=["pdf"],
            accept_multiple_files=True
        )
        
        if files is not None:
            st.write(f"You've uploaded {len(files)} files:")

            valid_pdfs=[]
            invalid_files = []

            with st.spinner("Processing Files........."):

                for file in files:
                    # Read the first 4 bytes (file signature)
                    file_signature = file.read(4)
                    file.seek(0)  # Reset the file pointer

                    # Check if the file signature matches the PDF signature
                    if file_signature == b"%PDF":
                        valid_pdfs.append(file)
                    else:
                        invalid_files.append(file)
                        st.error(f"File '{file.name}' is not a valid PDF.",icon="🚫")

                st.write(f"Valid PDF files ({len(valid_pdfs)}):")

                upload_folder = "uploads"

                # Create the "uploads" folder if it doesn't exist
                if not os.path.exists(upload_folder):
                    os.makedirs(upload_folder)

                for pdf in valid_pdfs:
                    with open(os.path.join(upload_folder, pdf.name), "wb") as f:
                        f.write(pdf.read())
            st.session_state["processed"]=True

        if st.button("Log Out"):
            st.session_state.clear()
            st.cache_data.clear()
            st.experimental_rerun()

    st.write("Welcome to,")
    st.image("logo.png",width=200)
    st.write("Upload your Pdfs in the sidebar to continue....")
    st.markdown("")
    st.experimental_rerun()


def read_docs():
    with st.spinner("Reading Documents........"):    
            if not (st.session_state.get("chain_created")) and st.session_state.get("processed"):
                db = create_db("uploads")
                st.session_state["qa"] = create_chain(clarifai_llm, db)
                st.session_state["chain_created"] = True
