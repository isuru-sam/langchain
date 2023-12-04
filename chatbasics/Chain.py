from langchain.chat_models import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from langchain.chains  import LLMChain
llm = ChatOpenAI(temperature=0.9)
prompt=ChatPromptTemplate.from_template("What is the best name to describe a company that makes a {product}")
chain=LLMChain(llm=llm,prompt=prompt)
product="office chair"
print(chain.run(product=product))