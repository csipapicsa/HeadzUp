import streamlit as st
from functions import load_style_css

st.set_page_config(layout="wide")

def main():
# Define the custom styles for the buttons and flex container
    button_style = """
    <style>
    .flex-container {
        display: flex;
        justify-content: center;
        align-items: center;
        height: 50vh;
    }
    .flex-item {
        flex: 1;
        margin: 5px; /* Adjust the margin as you like */
        text-align: center;
        height: 50%; /* You can adjust the height */
        background-color: #4CAF50;
        color: white;
        display: flex;
        justify-content: center;
        align-items: center;
        border: none;
        padding: 0;
    }
    .flex-item:first-child {
        justify-content: flex-start;
        background-color: #4CAF50;
    }
    .flex-item:last-child {
        justify-content: flex-end;
        background-color: #F44336;
    }
    button {
        width: 100%;
        height: 100%;
        border: 3px solid black;
        border-radius: 5px;
        font-size: 20px;
    }
    </style>
    """

    # Add the custom styles to the page
    st.markdown(button_style, unsafe_allow_html=True)

    # Create two columns for the buttons with a flexbox container
    col1, col2 = st.columns(2)

    # Place a button in each column within a flex-item div
    with col1:
        st.markdown(
            """<div class="flex-container">
                <div class="flex-item">
                    <button onclick="alert('Button 1 clicked')">Button 1</button>
                </div>
            </div>""", 
            unsafe_allow_html=True
        )

    with col2:
        st.markdown(
            """<div class="flex-container">
                <div class="flex-item">
                    <button onclick="alert('Button 2 clicked')">Button 2</button>
                </div>
            </div>""", 
            unsafe_allow_html=True
        )

    # Center text below the buttons
    st.markdown("<h1 style='text-align: center;'>Here is some text</h1>", unsafe_allow_html=True)


# if main
if __name__ == "__main__":
    main()
    
