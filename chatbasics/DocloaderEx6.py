from langchain.chains import RetrievalQA
from langchain.chat_models import ChatOpenAI
from langchain.document_loaders import CSVLoader
from langchain.vectorstores import DocArrayInMemorySearch
from IPython.display import display,Markdown
from langchain.indexes import VectorstoreIndexCreator
from langchain.embeddings import OpenAIEmbeddings
file="bookstores.csv"
loader=CSVLoader(file_path=file)
docs=loader.load()
embeddings=OpenAIEmbeddings()
embed=embeddings.embed_query("Hi my name is harrison")
print(len(embed))

db=DocArrayInMemorySearch.from_documents(docs,embeddings)
query="Please suggest a bookstore close to colombo"
docs = db.simillarity_search(query)
list(docs)
retriever=db.as_retriever()
llm=ChatOpenAI(temperature=0.0)
qdocs="".join([docs[i].page_content for i in range(len(docs))])
response=llm.call_as_llm(f"{qdocs} Question:list all books written by Mark")
display(Markdown(response))

index   =VectorstoreIndexCreator(vectorstore_cls=DocArrayInMemorySearch).from_loaders([loader])
query="Please list all boooks price greater than 100"
response = index.query(query)
display(Markdown(response))