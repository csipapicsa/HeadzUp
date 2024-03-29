import streamlit as st

if st.button("Page 1"):
    st.switch_page("pages/page_1_good.py")
if st.button("Page 2"):
    st.switch_page("pages/page_2.py")
if st.button("Page 3"):
    st.switch_page("pages/page_3.py")
if st.button("Page 4"):
    st.switch_page("pages/page_4.py")