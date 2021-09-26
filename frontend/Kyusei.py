import streamlit as st
import numpy as np
import pandas as pd
import time
from PIL import Image

page_bg_img = '''
<style>
body {
background-image: url("https://images.unsplash.com/photo-1445905595283-21f8ae8a33d2?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1173&q=80");
background-size: cover;
}
</style>
'''

st.markdown("""
<style>
.color-font {
    font-size:100px !important;
    color: "red";
}
.color-font2 {
    font-size:30px !important;
    color: "white";
    
}
</style>
""", unsafe_allow_html=True)
st.markdown('<p class="color-font"><font color = "white">Kyusei</font></p>',
            unsafe_allow_html=True)


st.markdown('<p class="color-font2" ><font color = "white">Repositories</font></p>',
            unsafe_allow_html=True)
# for i in range(5):
repo_names = ['requests', 'scrapy', 'fastapi', 'rich', 'textual', 'httpx', 'pydantic', 'tqdm', 'bokeh', 'sanic', 'dash', 'mangadex', 'pyseto', 'Slicer', 'pytago', 'earthquakes',
              'dvc', 'aiospotify', 'ray', 'ruck', 'quimb', 'fileseq', 'Lean', 'merk', 'pe', 'Ignition', 'Cura', 'nextpnr', 'onlineshop', 'labyrinth', 'sentry', 'flask', 'httpie']

button_array = [st.checkbox(i) for i in repo_names]

if st.button("Submit"):
    arr = [repo_names[i] for i in range(len(repo_names)) if button_array[i]]
    st.write(arr)

image_array = ['images//color//3-cloudclimate.jpg', 'images//color//download.jpg',
               'images//color//Eye_of_the_storm.jpg', 'images//color//unnamed.png']


# image5 = Image.open('images//color//3-cloudclimate.jpg')
i = 0
j = len(image_array)
while True:
    st.image(image_array[i])
    time.sleep(0.05)
    if i < j:
        i += 1
    else:
        i = 0
