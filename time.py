import streamlit as st

from datetime import datetime, timedelta


def time_left(end_time):
    # Calculate the time left until the end_time
    return max(int((end_time - datetime.now()).total_seconds()), 0)