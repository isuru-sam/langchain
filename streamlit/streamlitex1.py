import streamlit as st
import time
import pandas as pd
st.title("Hello streamlit world")
my_select_box=st.sidebar.selectbox("Select country:",list(["US","UK","LK","IN","RU"]))
my_slider=st.sidebar.slider("Temperature C")
st.sidebar.write(f'Temperature F:{my_slider*1.8+32}')