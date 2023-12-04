import openai

from langchain.prompts import PromptTemplate
from langchain.chat_models import ChatOpenAI
from langchain.chains import LLMChain
from llmapi import get_completion


summary_template =f"""
Generate a list of 3 book titles 
along with their author and genres.
Provide them in json format with below fields.
bookid,title,author,genre.
"""
print(get_completion(summary_template))
