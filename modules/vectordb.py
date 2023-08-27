from langchain.vectorstores import Clarifai as Clarifai_vectordb
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.document_loaders import PyPDFDirectoryLoader
from langchain.vectorstores import Chroma, FAISS
from modules.models import *

def create_db(pdfs_folde_path):

    loader = PyPDFDirectoryLoader(pdfs_folde_path)
    pages = loader.load()

    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=0)

    docs = text_splitter.split_documents(pages)
    print(docs[0])

    # persist_directory = 'db'

    # vector_db = Chroma.from_documents(documents=docs,
    #                                 embedding=clarifai_embedding_model,
    #                                 persist_directory=persist_directory)


    # vector_db = Clarifai_vectordb.from_documents(
    #     user_id=st.secrets["USER_ID"],
    #     app_id=st.secrets["APP_ID"],
    #     documents=docs,
    #     pat=st.secrets["CLARIFAI_PAT"],
    #     number_of_docs=2,
    # )
    if len(docs)<1:
        raise Exception("No Documents created")
    else:
        vector_db = FAISS.from_documents(docs, clarifai_embedding_model)
    
    return vector_db