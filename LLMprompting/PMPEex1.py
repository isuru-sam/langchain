import openai

from langchain.prompts import PromptTemplate
from langchain.chat_models import ChatOpenAI
from langchain.chains import LLMChain
import os

openai.api_key="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"

def get_completion(summary_template,text="",model="gpt-3.5-turbo"):
    summary_prompt_template = PromptTemplate(input_variables=["text"], template=summary_template)
    llm = ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo")
    chain = LLMChain(llm=llm, prompt=summary_prompt_template)
    return chain.run(text=text)


text = """
    srilanka is in asia.capital is colombo.
    It is situated from indian ocean.
    It is famous for its ancient ruins and beautiful landscapes.
    Srilanka has beautiful rivers and canals flowing covering many parts of the island.
    There are hills and mountains which add to the beauty of this country.
    """
summary_template =f"""
Summarize the text delimited by triple backticks into a single sentence.
'''{text}'''
"""
print(get_completion(summary_template,text))