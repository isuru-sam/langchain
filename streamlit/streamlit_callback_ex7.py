import streamlit as st
st.subheader("distance converter")

def miles_to_km() :
    st.session_state.km=st.session_state.miles*1.6

def km_to_miles() :
    st.session_state.miles=st.session_state.km*0.625

col1,buf,col2 = st.columns([2,1,2])
with col1:
    miles=st.number_input("Miles",key="miles",on_change=miles_to_km)
with col2:
    km=st.number_input("Km",key="km",on_change=km_to_miles)