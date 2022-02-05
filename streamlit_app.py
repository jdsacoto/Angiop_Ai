#dashboard
print("Hello world")
pip install streamlit
streamlit hello
import streamlit as st

x = st.slider('Select a value')
st.write(x, 'squared is', x * x)
