#dashboard
print("Hello world")
#pip install streamlit
#streamlit hello
import streamlit as st
# importing matplotlib modules
from PIL import Image



img = Image.open("Angio.png")
st.image(img)
st.write(
"""
# ANGIOP.AI
"""
)




"""
It's our pleasure to introduce you ANGIOP.AI, an Artificial Intelligence model which converts simple angiography images into contrasted images.
"""


"""
## File Uploader
It's hard to test the ability to upload files in an automated way, so here you
should test it by hand. Please upload a Zip file and make sure it is the correct file.
"""

w = st.file_uploader("Upload a DCM.zip file", type="zip")
if w:
    import pandas as pd

    data = pd.read_csv(w)
    st.write(data)
"""
## File Downloader
You can download the new .Zip file with contrasted images.
"""    
"""
if st.button('Run model'):
     st.write('Model is Running')
 else:
     st.write('Model is stopped')
text_contents = "Model Finished"
"""
# Different ways to use the API

st.download_button('Download ZIP', text_contents, 'text/zip')
