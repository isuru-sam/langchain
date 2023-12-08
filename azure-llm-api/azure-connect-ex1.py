import os
import openai
from langchain.llms import AzureOpenAI
from langchain.prompts import PromptTemplate
from langchain.chat_models import ChatOpenAI
from langchain.chains import LLMChain
openai.api_type = "azure"
openai.api_base = "https://isuru-openai.openai.azure.com/"
openai.api_version = "2023-07-01-preview"
openai.api_key = os.getenv("OPENAI_API_KEY")
llm = AzureOpenAI(
    deployment_name="gpt-35-turbo",
    model_name="gpt-35-turbo"
)
text = """
    srilanka has beautiful rivers and canals flowing covering many parts of the island.
    There are hills and mountains which add to the beauty of this country.
    Srilanka is famous for cricket and once they became world champions.

    """
summary_template = f"""
Assume you an article writer.
Identify the emotions writer is expressing in the review about Srilanka.

Use the text delimited by <> 
<{text}>
"""
summary_prompt_template = PromptTemplate(input_variables=["text"], template=summary_template)
#https://github.com/easonlai/azure_openai_langchain_sample/blob/main/chat_with_pdf.ipynb
# Run the LLM
chain = LLMChain(llm=llm, prompt=summary_prompt_template)
result= chain.run(text=text)
print(result)
