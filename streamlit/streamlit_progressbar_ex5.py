import streamlit as st
import time
import pandas as pd
st.write("Start extensive computation")
latest_iteration = st.empty()
progress_text="Opearation in progress please wait"
my_bar=st.progress(0,text=progress_text)
time.sleep(2)

for i in range(100):
    my_bar.progress(i+1)
    latest_iteration.text(f'iteration{i+1}')
    time.sleep(0.1)

st.write('we are done')