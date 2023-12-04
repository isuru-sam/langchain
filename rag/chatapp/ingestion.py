from langchain.document_loaders import ReadTheDocsLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import Pinecone
from langchain import OpenAI
from langchain.chains import RetrievalQA
import os
import pinecone
pinecone.init(api_key="08ca8063-1c86-4ac3-935c-c4242a0ab274",environment="gcp-starter")

OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")



def ingestdocs()->None:
    loader=ReadTheDocsLoader(path="/home/isuru/virtusa.udemy.com/langchaindocs/langchain-docs/api.python.langchain.com/en/latest")
    print("start loading")
    row_documents = loader.load()
    print("end loading")
    print(f"loaded{len(row_documents)}")
    text_splitter=RecursiveCharacterTextSplitter(chunk_size=500,chunk_overlap=50,separators=["\n\n","\n"," ",""])
    documents= text_splitter.split_documents(documents=row_documents)
    for doc in documents:
        old_path=doc.metadata["source"]
        new_url=old_path.replace("langchain-docs","https:/")
        doc.metadata.update({"source": new_url})
    print(f"going to insert{len(documents)} documents into pinecorn")
    embeddings =OpenAIEmbeddings()
    Pinecone.from_documents(documents=documents,embedding=embeddings,index_name="medium-blog-embedding-index")
    print("Added to pinecorn")
if __name__ == '__main__':
    ingestdocs()