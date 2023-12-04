

from langchain.prompts import PromptTemplate
from langchain.chat_models import ChatOpenAI
from langchain.chains import LLMChain
import os

def get_completion(summary_template,text="",model="gpt-3.5-turbo",temperature=0):
    summary_prompt_template = PromptTemplate(input_variables=["text"], template=summary_template)
    llm = ChatOpenAI(temperature=temperature, model_name="gpt-3.5-turbo")
    chain = LLMChain(llm=llm, prompt=summary_prompt_template)
    return chain.run(text=text)