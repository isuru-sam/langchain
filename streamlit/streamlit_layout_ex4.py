import streamlit as st
import time
import pandas as pd
from io import StringIO
import random
cities=["London","Colombo","Paris","Newyork"]
city=st.sidebar.selectbox("City",cities,index=2)
slider = st.sidebar.slider("Tmperature")
left_column,right_column= st.columns(2)

data = [random.random() for _ in range (100)]
with left_column:
    st.subheader('A line chart')
    st.line_chart(data)
right_column.subheader('Data')
right_column.write(data[:10])
col1,col2,col3=st.columns([0.2,0.5,0.3])
col1.markdown('Hello streamlit world')
col2.write(data[5:10])
with col3:
    st.header("cat")
    st.image("https://static.streamlit.io/examples/cat.jpg")
with st.expander("Click to expand"):
    st.bar_chart({'Data':[random.randint(2,10) for _ in range(25)]})
    st.write("This is image of dog")
    st.image("https://static.streamlit.io/examples/dog.jpg")