from langchain.chains import RetrievalQA
from langchain.chat_models import ChatOpenAI
from langchain.document_loaders import CSVLoader
from langchain.indexes import VectorstoreIndexCreator
from langchain.vectorstores import DocArrayInMemorySearch
file="bookstores.csv"
loader=CSVLoader(file_path=file)
docs=loader.load()
index   =VectorstoreIndexCreator(vectorstore_cls=DocArrayInMemorySearch).from_loaders([loader])
llm=ChatOpenAI(temperature=0.0)
qa=RetrievalQA.from_chain_type(llm=llm,chain_type="stuff",retriever=index.vectorstore.as_retriever(),verbose=True,chain_type_kwargs={"document_seperator":"<<<<>>>>"})