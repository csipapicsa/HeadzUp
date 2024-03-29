import streamlit as st
import random
import time
from datetime import datetime, timedelta
import threading
# from time import sleep

print("---------------------")


def main():
    try:
        print(st.session_state.page)
    except:
        None
    if "page" not in st.session_state:
        st.session_state.page = "main"
        main_page()
    elif st.session_state.page == "main":
        main_page()
    elif st.session_state.page == "game":
        game()


def main_page():

    if st.session_state.page == "main":

        st.title('Heads Up!')

        st.write('This is a simple game of Heads Up! where you have to guess the word on the card.')
        st.write('You can choose from the following categories:')
        categories = ['Animals', 'Movies', 'Countries', 'Fruits', 'Objects']
        st.session_state.length_of_the_game = st.number_input('Enter the length of the game in seconds', min_value=10, max_value=30, value=10)
        category = st.selectbox('Select a category', categories)


        words = []
        if category == 'Animals':
            st.session_state.words = ['Dog', 'Cat', 'Elephant', 'Giraffe', 'Lion', 'Tiger', 'Zebra', 'Monkey', 'Penguin', 'Kangaroo']
        elif category == 'Movies':
            st.session_state.words = ['Inception', 'Interstellar', 'The Dark Knight', 'The Matrix', 'The Godfather', 'The Shawshank Redemption', 'The Lord of the Rings', 'The Avengers', 'The Lion King', 'The Terminator']
        elif category == 'Countries':
            st.session_state.words = ['Australia', 'Brazil', 'Canada', 'China', 'France', 'Germany', 'India', 'Italy', 'Japan', 'United States']
        elif category == 'Fruits':
            st.session_state.words = ['Apple', 'Banana', 'Cherry', 'Grapes', 'Kiwi', 'Mango', 'Orange', 'Peach', 'Pineapple', 'Strawberry']
        else:
            st.session_state.words = ['Chair', 'Table', 'Lamp', 'Book', 'Computer', 'Phone', 'Television', 'Refrigerator', 'Microwave', 'Washing Machine']

        # Start the game
        if st.button('Start Game'):
            # Initialize the game state
            st.session_state.game_started = True
            st.session_state.score = 0
            st.session_state.current_word = random.choice(st.session_state.words)
            st.session_state.placeholder_word = st.empty()
            st.session_state.placeholder_time = st.empty()
            st.session_state.placeholder_info = st.empty()
            st.session_state.page = "game"
            
            st.rerun()


def game():
    if "timer_bool" not in st.session_state:
        st.session_state.start_time = time.time()
        st.session_state.end_time = st.session_state.start_time + 10  # 10 seconds from now
        st.session_state.timer_bool = False

        # Layout for buttons
    col1, col2 = st.columns([1,1])

    with col1:
        if st.button('Correct!', key='correct'):
            # Update score or game state as needed
            st.session_state.score += 1
            st.session_state.current_word = random.choice(st.session_state.words)  # Assuming 'words' list is defined globally

    with col2:
        if st.button('Pass', key='pass'):
            # Update game state as needed
            st.session_state.current_word = random.choice(st.session_state.words)  # Assuming 'words' list is defined globally


  # Game logic
    while not st.session_state.timer_bool:
        st.session_state.placeholder_word.write(f'Current word: {st.session_state.current_word}')
        st.session_state.placeholder_info.write('The game is on!')
        time.sleep(0.20)  # Simulate game processing delay
        st.session_state.placeholder_time.write(f'Time left: {int(st.session_state.end_time - time.time())} seconds')


        if time.time() > st.session_state.end_time:
            st.write('Time is up!')
            st.session_state.timer_bool = True
            del st.session_state.timer_bool
            st.session_state.page = "main"
            break

        

# Starting point of the app
if 'timer' not in st.session_state:
    st.session_state.timer = False

main()