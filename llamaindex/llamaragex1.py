import os

from langchain.chat_models import ChatOpenAI
from llama_index import SimpleDirectoryReader
from llama_index import Document
from llama_index import VectorStoreIndex
from llama_index import ServiceContext
from llama_index.llms import OpenAI
from trulens_eval import Tru
from utils import   get_prebuilt_trulens_recorder
OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")
documents = SimpleDirectoryReader(input_files=["/home/isuru/virtusa.udemy.com/pinecone/vectordata.pdf"]).load_data()
document = Document(text="\n\n".join([doc.text for doc in documents]))
print(len(documents))
#print(document.text)
llm = ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo")
service_context=ServiceContext.from_defaults(llm=llm,embed_model="local:BAAI/bge-small-en-v1.5")
index=VectorStoreIndex.from_documents([document],service_context=service_context)
query_engine = index.as_query_engine()
response = query_engine.query("What is a Vector database")
print(str(response))
eval_questions=["What is a vector db","What is pinecone","what is embedding","what is index","what is searching","what is augumenting","what is retrieving","Does context relavant to response"]
tru=True()
tru.reset_database()
tru_recorder = get_prebuilt_trulens_recorder(query_engine,app_id="VectorDb")
with tru_recorder as recording:
    for question in eval_questions:
        response=  query_engine.query(question)

records,feedback=tru.get_records_and_feedback(app_ids=[])
records.head()