import streamlit as st

import pandas as pd

import numpy as np

# st.write("Hello World")

# x = st.text_input("Favourite Movie? ")

# st.write(f"Your favourite movie is: {x}")

# data = pd.read_csv("movies.csv")

# st.write(data)

st.write("# My cool Chart")

chart_data = pd.DataFrame(
    np.random.randn(20,3),
    columns = ["a","b","c"]
)

st.bar_chart(chart_data)
st.line_chart(chart_data)



