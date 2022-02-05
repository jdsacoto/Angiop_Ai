#dashboard
print("Hello world")
#pip install streamlit
#streamlit hello
import streamlit as st

"""
# File Uploader
##Equipo Rosa
It's hard to test the ability to upload files in an automated way, so here you
should test it by hand. Please upload a Zip file and make sure a table shows up
below with its contents.
"""


"""
## File Uploader
It's hard to test the ability to upload files in an automated way, so here you
should test it by hand. Please upload a Zip file and make sure a table shows up
below with its contents.
"""

w = st.file_uploader("Upload a DCM.zip file", type="zip")
if w:
    import pandas as pd

    data = pd.read_csv(w)
    st.write(data)
"""
## File Downloader
It's hard to test the ability to upload files in an automated way, so here you
should test it by hand. Please upload a Zip file and make sure a table shows up
below with its contents.
"""    
# Text files

text_contents = '''
Foo, Bar
123, 456
789, 000
'''

# Different ways to use the API

st.download_button('Download CSV', text_contents, 'text/csv')
