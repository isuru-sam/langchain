
from langchain.prompts import PromptTemplate
from langchain.chat_models import ChatOpenAI
from langchain.chains import LLMChain
import os
import streamlit as st
import time
import pandas as pd
def get_completion(summary_template,text="",model="gpt-3.5-turbo",temperature=0):
    summary_prompt_template = PromptTemplate(input_variables=["text"], template=summary_template)
    llm = ChatOpenAI(temperature=temperature, model_name="gpt-3.5-turbo")
    chain = LLMChain(llm=llm, prompt=summary_prompt_template)
    return chain.run(text=text)

def sentiment_analyer(text:str):
    emotions = "positive,negative"
    emotions = "happy,sad,angry,mad,tired,very happy,very sad,very angry,very tired,very mad"

    summary_template = f"""
    What is the sentiment of the given review about text.
    Sentiment s should be only with emotions {emotions}
    Use the text delimited by <> 
    <{text}>
    """
    return get_completion(summary_template,text)


print(sentiment_analyer(""))

col1,col2 =st.columns([0.85,0.15])
with col1:
    st.title("zero shot sentiment analysis")
with col2:
    st.image("ai.jpeg",width=70)
with st.form(key="my+form"):
    default_emotions = "posiive,negative,neutral"
    default_emotions = "happy,sad,angry,mad,tired,very happy,very sad,very angry,very tired,very mad"


    emotions=st.text_input("Emotions:",value=default_emotions)
    text=st.text_area(label="Text to classify")
    # text = """   It was a rainy day.I could not play cricket.    """
    # text="""Putin invaded ukraine"""
    # text="""it was exhausting to work over night"""
    # text="he jumped out from 3000 feet tall building"
    #text = """he won 10000$ from a lottery"""
    submit_button=st.form_submit_button(label="Check")
    if submit_button:
        emotion=sentiment_analyer(text)
        result=f"{text} => {emotion}\n"
        st.write(result)
        st.divider()
        if 'history' not in st.session_state:
            if result:
                st.session_state['history']=result
            else:
                st.session_state['history']=''
        else:
            st.session_state['history']+=result

        if st.session_state['history']:
            st.text_area(label='history',value=st.session_state['history'],height=400)