from langchain.document_loaders import TextLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import Pinecone
from langchain import OpenAI
from langchain.chains import RetrievalQA
import os
import pinecone
pinecone.init(api_key="08ca8063-1c86-4ac3-935c-c4242a0ab274",environment="gcp-starter")

OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")



loader =TextLoader("/home/isuru/virtusa.udemy.com/pinecone/vectordatabase")
document=loader.load()
print(document)
textsplitter=CharacterTextSplitter(chunk_size=1000,chunk_overlap=0)
texts=textsplitter.split_documents(document)
print(len(texts))
embeddings = OpenAIEmbeddings(openai_api_key=OPENAI_API_KEY)
docsearch=Pinecone.from_documents(texts,embeddings,index_name="medium-blog-embedding-index")
qa=RetrievalQA.from_chain_type(llm=OpenAI(),chain_type="stuff",retriever=docsearch.as_retriever())
query="What is a Vector DB? give me a 15 word answer for a beginner"
result=qa({"query":query})
print(result)
