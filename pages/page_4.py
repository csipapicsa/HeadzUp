import streamlit as st
from functions import load_style_css

st.set_page_config(layout="wide")

def main():
# Define the custom styles for the buttons and flex container
# Create two columns for the buttons
    col1, col2 = st.columns(2)

    # Button in the first column with custom color
    with col1:
        if st.button("Button Green", key='1'):
            st.session_state.button_color = 'green'
            # Perform action for Button 1
            st.write("Green button was clicked")

    # Button in the second column with custom color
    with col2:
        if st.button("Button Red", key='2'):
            st.session_state.button_color = 'red'
            # Perform action for Button 2
            st.write("Red button was clicked")

    # Use session state to set button colors
    if 'button_color' not in st.session_state:
        st.session_state.button_color = None  # Default value if no button has been clicked yet

    # Define the custom styles for the buttons based on session state
    button_style = f"""
    <style>
    div.stButton > button {{
        width: 100%; /* Full width */
        height: 50vh; /* 50% of the viewport height */
        border: 3px solid black;
        border-radius: 5px;
        font-size: 20px;
    }}
    /* Style for the green button */
    {"div.stButton > button:nth-of-type(1) {background-color: #4CAF50; color: white;}" if st.session_state.button_color == 'green' else ""}
    /* Style for the red button */
    {"div.stButton > button:nth-of-type(2) {background-color: #F44336; color: white;}" if st.session_state.button_color == 'red' else ""}
    </style>
    """

    # Add the custom styles to the page
    st.markdown(button_style, unsafe_allow_html=True)

    # Center text below the buttons
    st.markdown("<h1 style='text-align: center;'>Here is some text</h1>", unsafe_allow_html=True)


# if main
if __name__ == "__main__":
    main()
    
