from langchain.prompts import PromptTemplate
from langchain.chat_models import ChatOpenAI
from langchain.agents import initialize_agent, Tool, AgentType
from tools.tools import get_profile_url


def lookup(name: str) -> str:
    input_template = """
    Given the  full name {name_of_person} I want you to get me a link to their Linked in profile page.
    Answer should contain only a url.
    """
    llm = ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo")
    tools_for_agent = [
        Tool(
            name="Crawl Google 4 linkedin profile page",
            func=get_profile_url,
            description="Useful to fetch linkedin profile link by name",
        )
    ]
    agent = initialize_agent(
        tools=tools_for_agent,
        llm=llm,
        agent=AgentType.CHAT_ZERO_SHOT_REACT_DESCRIPTION,
        verbose=True
    )

    prompt_template = PromptTemplate(
        input_variables=["name_of_person"], template=input_template
    )
    # temprature 0 means 0 creativity

    linked_profile_url = agent.run(prompt_template.format_prompt(name_of_person=name))
    return linked_profile_url
