import streamlit as st
import numpy as np
import pandas as pd
import time
from PIL import Image
from make_clusters import compute_clusters
from plot_universe import generate_galaxies, plot_stars
import matplotlib.pyplot as plt

st.markdown("""
<style>
.color-font {
    font-size:100px !important;
    color: "red";
}
</style>
""", unsafe_allow_html=True)
st.markdown('<p class="color-font">Kyusei</p>', unsafe_allow_html=True)

st.write("Our project ‘Kyusei’ takes the popular static analysis tool Metabob API and makes it a more personalized tool for upcoming python developers and data science enthusiasts. Static analysis is used for software development and quality assurance teams to check for vulnerabilities. What we aim to promote through our project is the mindset that even young developers or non-professionals can go through their repo's and do debugging/error analysis using automated tools. Not only will this help the developers, but it will help in popularizing the metabob API among the developing community. The next generation of python developers should be aware of such tools which expose security vulnerabilities and other common errors in their personal as well as professional endeavors, not to mention automated static analysis tools, are the future of debugging and a tool all developers should be familiar with.")

st.subheader("Repositories")
repo_names = ['requests', 'scrapy', 'fastapi', 'rich', 'textual', 'httpx', 'pydantic', 'tqdm', 'bokeh', 'sanic', 'dash', 'mangadex', 'pyseto', 'Slicer', 'pytago', 'earthquakes',
              'dvc', 'aiospotify', 'ray', 'ruck', 'quimb', 'fileseq', 'Lean', 'merk', 'pe', 'Ignition', 'Cura', 'nextpnr', 'onlineshop', 'labyrinth', 'sentry', 'flask', 'httpie']

col1, col2, col3 = st.columns(3)
t = len(repo_names)//3
button_array = [col1.checkbox(i) for i in repo_names[:t]] + [col2.checkbox(i) for i in repo_names[t:2*t]] + [col3.checkbox(i) for i in repo_names[2*t:]]

if st.button("Submit"):
    arr = [repo_names[i] for i in range(len(repo_names)) if button_array[i]]
    if len(arr)<5:
        eps = 0.05
    elif len(arr)<10:
        eps = 0.035
    elif len(arr)<15:
        eps=0.015
    else:
        eps=0.0075
    repos = arr
    results_clusters = compute_clusters(arr)
    base_angle = np.pi*np.random.random()
    points_arr, centroid_arr, keys_arr = generate_galaxies(results_clusters, base_angle=base_angle)
    plot_stars(points_arr, centroid_arr, keys_arr, repos)
    keys_arr = [i.T[:2] for i in keys_arr]
    st.markdown("## Presenting Similar Issues:")
    for keys in keys_arr:
        df = pd.DataFrame(keys.T)
        df.columns = ['Repository Name', 'Ref ID']
        st.write(df)
    i = 0
    st.markdown("## A Spa-ce-ial Representation of these Embeddings:")
    imageLocation = st.empty()
    for _ in range(int(2*np.pi//0.05)):
        imageLocation.image('stars.png')
        points_arr, centroid_arr, keys_arr = generate_galaxies(results_clusters, base_angle=base_angle+i*0.05)
        plot_stars(points_arr, centroid_arr, keys_arr, repos)
        time.sleep(0.05)
        i += 1