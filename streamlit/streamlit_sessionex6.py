import streamlit as st
import time

import streamlit as st
st.title("Streamlit session")
st.write(st.session_state)
if 'counter' not in st.session_state:
    st.session_state['counter']=0
else:
    st.session_state['counter']= st.session_state['counter']+1

number =st.slider('Value',1,10,key="my_slider")