from langchain.chat_models import ChatOpenAI
from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferMemory
from langchain.memory import ConversationSummaryBufferMemory
llm = ChatOpenAI(temperature=0.0)
memory=ConversationSummaryBufferMemory(llm=llm,max_token_limit=400)
memory.save_context({"input":"context"})



conversation=ConversationChain(llm=llm,memory=memory,verbose=True)
ex1=conversation.predict(input="Hi Ia m Isuru")
print(ex1)
ex1=conversation.predict(input="What is my name")
print(ex1)
print(memory.buffer)