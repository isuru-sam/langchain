import streamlit as st
import time
import pandas as pd
from io import StringIO
name = st.text_input("Your name: ")
if name:
    st.write(f"Hello {name}")
x=st.number_input("Enter a number ",min_value=1,max_value=99,step=1)
st.write(f"Current number is {x}")
st.divider()
clicked = st.button("Click me")
st.divider()
agree=st.checkbox("i agree")
agree=st.checkbox("continue",value=True)

df=pd.DataFrame({"Name":["Anne","Maria","Douglase","Jane"],"Age":[10,20,30,40]})
if st.checkbox("Show Data"):
    st.write(df)
pets=["cats","dogs","fish","turtle"]
pet=st.radio("Favourite pet",pets,index=2,key="your_pet")
st.write(pet)
cities=["London","Colombo","Paris","Newyork"]
city=st.selectbox("City",cities,index=2)
st.write(city)

st.divider()
x=st.slider('x',value=15,min_value=10,max_value=100,step=1)
st.write(x)
st.divider()
uploaded_file=st.file_uploader("Upload file",type=["txt","csv","pdf"])
if uploaded_file:
    if uploaded_file.type=="text/plain":
        stringio= StringIO(uploaded_file.getvalue().decode('utf-8'))
        stringdata =stringio.read()
        st.write(stringdata)

st.divider()

camera_input=st.camera_input("Take a photo")
if camera_input:
    st.image(camera_input)

