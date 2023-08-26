# from langchain.retrievers.self_query.base import SelfQueryRetriever
# from langchain.chains.query_constructor.base import AttributeInfo

from langchain.chains import RetrievalQA

def create_chain(local_llm, vectordb):

    # memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)

    # metadata_field_info = [
    # AttributeInfo(
    #     name="source",
    #     description="The neme of pdf",
    #     type="string or list[string]",
    # ),
    # AttributeInfo(
    #     name="page",
    #     description="The page no of the pdf",
    #     type="integer",
    # ),
    # ]

    # document_content_description = "Information about the PDF's page and name of pdf"
    # retriever = SelfQueryRetriever.from_llm(
    #     local_llm, vectordb, document_content_description, metadata_field_info, verbose=False,
    #     search_kwargs={"fetch_k": 3}
    # )


    retriever = vectordb.as_retriever(search_type="mmr", search_kwargs={'fetch_k': 3})

    qa = RetrievalQA.from_chain_type(llm=local_llm,
                                     chain_type="stuff",
                                     retriever=retriever,
                                     return_source_documents=True,)


    qa.combine_documents_chain.llm_chain.prompt.template = '''
    Your name is Ash.
    Use the following pieces of context to answer the users question and that
    information consist of provided pdf details by user.
    If you don't know the answer, just apologies and say that you couldn't
    find relevent content to answer this question, don't try to
    make anything from yourself just use the provided context. And always answer
    in conversationl freindly way. And don't make any Follow-up Question and don't
    provide any further information just answer the question.
    Always answer from the perspective of being Ash.
    ----------------
    {context}

    Question: {question}
    Helpful Answer:'''
    return qa

# chat_history = []
# query = "when did I started my job at macroinception?"
# inputs = {
#             'query': query,
#             'chat_history': chat_history
#         }
# # chat_history.append((query, result['result']))

# result = qa(inputs, return_only_outputs=True)#qa.run(query)