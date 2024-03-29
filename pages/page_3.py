import streamlit as st
from functions import load_style_css

st.set_page_config(layout="wide")

def main():
# Define the custom styles for the buttons and flex container
    button_style = """
    <style>
    div.stButton > button {
        width: 100%; /* Full width */
        height: 50vh; /* 50% of the viewport height */
        border: 3px solid black;
        border-radius: 5px;
        font-size: 20px;
    }
    /* Style for the left button */
    div.stButton > button:first-of-type {
        background-color: #4CAF50; /* Green */
        color: white;
    }
    /* Style for the right button */
    div.stButton > button:last-of-type {
        background-color: #F44336; /* Red */
        color: white;
    }
    </style>
    """

    # Add the custom styles to the page
    st.markdown(button_style, unsafe_allow_html=True)

    # Create two columns for the buttons with a flexbox container
    col1, col2 = st.columns(2)

    # Place a button in each column within a flex-item div
# Place a button in each column and assign actions
    with col1:
        if st.button("Button Green", key='1',):
            # Perform action for Button 1
            st.write("Button 1 was clicked")

    with col2:
        if st.button("Button Red", key='2'):
            # Perform action for Button 2
            st.write("Button 2 was clicked")
        # Center text below the buttons
    st.markdown("<h1 style='text-align: center;'>Here is some text</h1>", unsafe_allow_html=True)


# if main
if __name__ == "__main__":
    main()
    
