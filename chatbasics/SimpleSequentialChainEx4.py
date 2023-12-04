from langchain.chat_models import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from langchain.chains import SimpleSequentialChain
from langchain.chains  import LLMChain
#"Use sequentialchain for complexx chaining"
#"Router chain"
llm = ChatOpenAI(temperature=0.9)
prompt=ChatPromptTemplate.from_template("What is the best name to describe a company that makes a {product}")
chain1=LLMChain(llm=llm,prompt=prompt,output_key="company_name")
prompt2=ChatPromptTemplate.from_template("Write a 20 rod description of the company:  {company_name}")
chain2=LLMChain(llm=llm,prompt=prompt2)
simplechain=SimpleSequentialChain(chains=[chain1,chain2],verbose=True,input_variables=["company_name"])

product="office chair"

simplechain.run(product=product)