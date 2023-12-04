from langchain.document_loaders import PyPDFLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import Pinecone
from langchain import OpenAI
from langchain.chains import RetrievalQA
import os
import pinecone
from langchain.vectorstores import FAISS
pinecone.init(api_key="08ca8063-1c86-4ac3-935c-c4242a0ab274",environment="gcp-starter")
OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")
pdfpath= "/home/isuru/virtusa.udemy.com/pinecone/vectordata.pdf"
loader =PyPDFLoader(pdfpath)
document=loader.load()
print(document)

textsplitter=CharacterTextSplitter(chunk_size=1000,chunk_overlap=30,separator="\n")
texts=textsplitter.split_documents(document)
print(len(texts))

embeddings = OpenAIEmbeddings(openai_api_key=OPENAI_API_KEY)
vectorstore=FAISS.from_documents(texts,embeddings)
vectorstore.save_local("faiss_index_react")
new_vector_Store =FAISS.load_local("faiss_index_react",embeddings)
dqa=RetrievalQA.from_chain_type(llm=OpenAI(),chain_type="stuff",retriever=new_vector_Store .as_retriever())
query="What is a Vector DB? give me a 15 word answer for a beginner"
result=dqa.run(query)
print(result)
