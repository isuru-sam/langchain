
from langchain.prompts import PromptTemplate
from langchain.chat_models import ChatOpenAI
from langchain.chains import LLMChain
import os
def get_completion(summary_template,text="",model="gpt-3.5-turbo",temperature=0):
    summary_prompt_template = PromptTemplate(input_variables=["text"], template=summary_template)
    llm = ChatOpenAI(temperature=temperature, model_name="gpt-3.5-turbo")
    chain = LLMChain(llm=llm, prompt=summary_prompt_template)
    return chain.run(text=text)
emotions="positive,negative"
emotions="happy,sad,angry,mad,tired,very happy,very sad,very angry,very tired,very mad"


#text = """   It was a rainy day.I could not play cricket.    """
#text="""Putin invaded ukraine"""
#text="""it was exhausting to work over night"""
#text="he jumped out from 3000 feet tall building"
text="""he won 10000$ from a lottery"""
summary_template = f"""
What is the sentiment of the given review about text.
Sentiment s should be only with emotions {emotions}
Use the text delimited by <> 
<{text}>
"""
print(get_completion(summary_template, text))