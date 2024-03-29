import streamlit as st

from functions import load_style_css

st.set_page_config(layout="wide")

# load_style_css("style_1.css")


col1, col_m, col2 = st.columns([1, 10, 1])

with col1:
    st.button("Click me left", type='primary')

with col2:
    st.button("Click me right", type='primary')