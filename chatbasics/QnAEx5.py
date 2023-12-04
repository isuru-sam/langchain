from langchain.chains import RetrievalQA
from langchain.chat_models import ChatOpenAI
from langchain.document_loaders import CSVLoader
from langchain.vectorstores import DocArrayInMemorySearch
from IPython.display import display,Markdown
from langchain.indexes import VectorstoreIndexCreator
file="bookstores.csv"
loader=CSVLoader(file_path=file)
index   =VectorstoreIndexCreator(vectorstore_cls=DocArrayInMemorySearch).from_loaders([loader])
query="Please list all boooks price greater than 100"
response = index.query(query)
display(Markdown(response))