import os

from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.chat_models import ChatOpenAI
from langchain.chains import RetrievalQA
from langchain.vectorstores import Pinecone
from langchain import OpenAI

import os
import pinecone
pinecone.init(api_key="08ca8063-1c86-4ac3-935c-c4242a0ab274",environment="gcp-starter")

OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")

def run_llm(query:str)-> any:
    embeddings=OpenAIEmbeddings()
    docsearch = Pinecone.from_existing_index(index_name="medium-blog-embedding-index",embedding=embeddings)
    chat=ChatOpenAI(verbose=True,temperature=0.0)
    qa=RetrievalQA.from_chain_type(llm=chat,chain_type="stuff",retriever=docsearch.as_retriever(),return_source_documents=True)
    return qa({"query":query})

if __name__=="__main__":
    print(run_llm(query="What is LangChain"))





