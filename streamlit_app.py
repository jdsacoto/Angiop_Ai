#dashboard
print("Hello world")
#pip install streamlit
#streamlit hello
import streamlit as st

x = st.slider('Select a value')
st.write(x, 'squared is', x * x)

"""
# File Uploader
It's hard to test the ability to upload files in an automated way, so here you
should test it by hand. Please upload a CSV file and make sure a table shows up
below with its contents.
"""

w = st.file_uploader("Upload a DCM.zip file", type="zip")
if w:
    import pandas as pd

    data = pd.read_csv(w)
    st.write(data)
