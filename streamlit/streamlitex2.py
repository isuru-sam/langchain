import streamlit as st
import time
import pandas as pd
st.title="Hello streamlit :100:"
st.write("Stream lit :100:")
l=[1,2,3]
st.write(l)
l2=list("abc")

l3=dict((zip(l,l2)))
st.write(l3)
df=pd.DataFrame({"first_column":[1,2,3,4],"second_column":list("abcd")})
df
