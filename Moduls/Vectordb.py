from langchain.vectorstores import Clarifai as Clarifai_vectordb
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.document_loaders import PyPDFDirectoryLoader

def create_db(pdfs_folde_path):

    loader = PyPDFDirectoryLoader(pdfs_folde_path)
    pages = loader.load()

    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=0)

    docs = text_splitter.split_documents(pages)


    vector_db = Clarifai_vectordb.from_documents(
        user_id='ab00k',
        app_id='DocuChat',
        documents=docs,
        pat=CLARIFAI_PAT,
        number_of_docs=3,
    )
    return vector_db