import os
from langchain.chains import LLMChain
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.utilities.dalle_image_generator import DallEAPIWrapper
OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")
llm = OpenAI(temperature=0.9)
prompt = PromptTemplate(
    input_variables=["image_desc"],
    template="Generate a detailed prompt to generate an image based on the following description: {image_desc}",
)
chain = LLMChain(llm=llm, prompt=prompt)
image_url = DallEAPIWrapper().run(chain.run("infront of taj samudra hotel sri lanka"))
print(image_url)
