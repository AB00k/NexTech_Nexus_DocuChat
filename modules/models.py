from langchain.llms import Clarifai
import streamlit as st

# Defining Models
Models = { 'llama2_70B': { 'USER_ID': 'meta',
                          'APP_ID': 'Llama-2',
                          'MODEL_ID': 'llama2-70b-chat'
                        },
            
            'cohere': { 'USER_ID': 'cohere',
                         'APP_ID': 'embed',
                         'MODEL_ID': 'cohere-text-to-embeddings'
                        }
}

# Initialize a LLM from Clarifai
clarifai_llm = Clarifai(
    pat=st.secrets["CLARIFAI_PAT"],
    user_id=Models['llama2_70B']['USER_ID'],
    app_id=Models['llama2_70B']['APP_ID'],
    model_id=Models['llama2_70B']['MODEL_ID']
)
