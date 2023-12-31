from langchain.prompts import PromptTemplate
from langchain.chat_models import ChatOpenAI
from langchain.chains import LLMChain
from third_parties.linkedin import scrape_linkedin_profile
from agents.linkedin_lookup_agent import lookup

if __name__ == "__main__":
    print("hello")
linkedin_profile_url = lookup(name="Isuru Samaraweera")
summary_template = """
given the linkedin information {information} about a person from I want to create:
 1.short summary
 2.two interesting facts about them

"""
summary_prompt_template = PromptTemplate(
    input_variables=["information"], template=summary_template
)
# temprature 0 means 0 creativity
llm = ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo")
chain = LLMChain(llm=llm, prompt=summary_prompt_template)

linkedin_data = scrape_linkedin_profile(
    linkedin_profile_url=linkedin_profile_url
)
print(chain.run(information=linkedin_data))
