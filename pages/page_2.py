import streamlit as st
from functions import load_style_css


def main():
    load_style_css("style_2.css")
    st.write("This is the second page of the app.")
    st.button("Click me", type='primary')



if __name__ == "__main__":
    main()